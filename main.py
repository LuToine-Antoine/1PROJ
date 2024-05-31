import tkinter as tk

from structures.board.board_struct import *
from structures.rings import *
from structures.pawn import *
from possibilites.ringsmoves import *
from possibilites.pawnsmoves import *


class Game:
    def __init__(self):
        self._rotation = None
        self._mode = None
        self._game_mode = None
        self._board = BoardStruct()
        self._round = 0
        self._player = 1
        self._ring_move_x = 0
        self._ring_move_y = 0
        self._clickCount = 0
        self.all_possibles_moves = []
        self._possibles = RingsMoves(0, 0, self._board.board)
        self._firstRing = Rings(0, 0, self._board.board)
        self._click_x = None
        self._click_y = None

    def set_game_mode(self, mode=0):
        self._game_mode = mode

    def get_game_mode(self):
        return self._game_mode

    def get_board(self):
        return self._board.board

    def get_player(self):
        return self._player

    def get_turn(self):
        return self._round

    def get_ring_player_1(self):
        return self._firstRing.get_player_1_ring()

    def get_ring_player_2(self):
        return self._firstRing.get_player_2_ring()

    def set_blitz_mode(self, mode=0):
        """
        True = blitz mode; False = normal mode
        """

        if mode == 1:
            self._game_mode = False  # Isn't blitz mode
        else:
            self._game_mode = True  # It's blitz mode

    def get_blitz_mode(self):
        return self._game_mode

    def win(self):
        """
        Check if a player win
        """
        board = BoardStruct()
        numberRing = Rings(0, 0, board.board)
        pawns = Paws(0, 0, board.board)
        pawnStock = pawns.pawns_stock(board.board)
        numberRingPlayer1 = numberRing.get_player_1_ring()
        numberRingPlayer2 = numberRing.get_player_2_ring()

        if not self._game_mode:
            numberToWin = 3
        else:
            numberToWin = 1

        # Check if a player win with check order by player turn
        if self._round % 2 == 0:  # Check win during player 1 turn
            if numberRingPlayer1 == numberToWin:
                return 1  # Player 1 win
            elif numberRingPlayer2 == numberToWin:
                return 2  # Player 2 win
            elif pawnStock:  # No pawns left
                if numberRingPlayer1 > numberRingPlayer2:
                    return 1  # Player 1 win
                elif numberRingPlayer2 > numberRingPlayer1:
                    return 2  # Player 2 win
                else:
                    return 3  # Equality

        elif self._round % 2 == 1:  # Check win during player 2 turn
            if numberRingPlayer2 == numberToWin:
                return 2  # Player 2 win
            elif numberRingPlayer1 == numberToWin:
                return 1  # Player 1 win
            elif pawnStock:  # No pawns left
                if numberRingPlayer2 > numberRingPlayer1:
                    return 2  # Player 2 win
                elif numberRingPlayer1 > numberRingPlayer2:
                    return 1  # Player 1 win
                else:
                    return 3  # Equality

        else:  # Nobody Win, game continue
            return False

    def game_loop(self, x, y):
        """
        Use to run the game
        """
        self._click_x = x
        self._click_y = y

        if self.in_board_verification(self._click_x, self._click_y):
            if self._round == 10:
                self._player = 1

            if self._player == 1:
                caseplayer = 2
            else:
                caseplayer = 3

            if self._round < 10:
                self.main_put_first_rings(self._click_x, self._click_y)

            elif self._round >= 10:
                if self._board.board[self._click_x][self._click_y] == caseplayer:
                    if self._clickCount == 0:
                        if self.main_put_pawns(self._click_x, self._click_y, self._player):
                            self.main_see_moves_rings()
                            self._clickCount = 1

                if self._clickCount == 1:
                    if self.main_move_rings(x, y, self._player):
                        self._board.see_board()
                        self._round += 1
                        if self._player == 1:
                            self._player = 2
                        else:
                            self._player = 1
                        self._clickCount = 0

            # Reset click
            self._click_x = None
            self._click_y = None

        # End of the game
        match self.win():
            case 1:
                print("Player 1 win")
            case 2:
                print("Player 2 win")
            case 3:
                print("Equality")
            case False:
                print("Game continue")

    def get_click_count(self):
        return self._clickCount

    def in_board_verification(self, x, y):
        """
        Use to check if the place selected is in the board
        """
        if 0 <= x < 19 and 0 <= y < 11:
            return True
        else:
            return False

    def main_put_first_rings(self, x, y):
        """
        Use to place 5 rings for each player at the start of the game
        """

        if not self.in_board_verification(x, y) or self._board.board[x][y] != 1:
            return False

        self._firstRing.put_rings(x, y, self._board.board, self._player)
        self._round += 1
        if self._player == 1:
            self._player = 2
        else:
            self._player = 1


    def main_put_pawns(self, x, y, player):
        """
        Use to place pawns on the board
        """
        pawns = Paws(x, y, self._board.board)

        # In order to check if place selected is a ring of good player
        if self._player == 1:
            player_case = 2
        else:
            player_case = 3

        if self.in_board_verification(x, y) and self._board.board[x][y] == player_case:
            pawns.put_paws(x, y, self._board.board, player)
            if player == 1:
                self._board.board[x][y] = 6
            else:
                self._board.board[x][y] = 7

            # Use to check automaticaly ring's possibilities
            self._ring_move_x = x
            self._ring_move_y = y

            return self._ring_move_x, self._ring_move_y
        else:
            return False

    def main_see_moves_rings(self):
        """
        Check all possibles moves for rings where player has put his pawn
        """
        self.all_possibles_moves.clear()
        # Get all possibles moves
        self._possibles.get_possible_moves(self._ring_move_x, self._ring_move_y)

        # Create a list of all possibles moves
        self.all_possibles_moves = self._possibles.get_vertical_moves() + self._possibles.get_diagonal_moves()
        print("Possible vertical : ", self._possibles.get_vertical_moves(), "Possible top left to bottom right : ", self._possibles.get_right_diagonal_moves(), self._possibles.get_left_diagonal_moves(), sep="\n")

        return self.all_possibles_moves

    def main_move_rings(self, x, y, player):
        """
        Use to choose ring's destination
        """
        self._rotation = PawnRotate(self._board.board)

        if not self.in_board_verification(x, y) or self._board.board[x][y] != 1 or (x,y) not in self.all_possibles_moves:
            return False

        print(x,y, self._possibles.get_vertical_moves())

        if (x, y) in self._possibles.get_vertical_moves():
            self._rotation.vertical_rotate(self._ring_move_y, self._ring_move_x, x)
        elif (x, y) in self._possibles.get_right_diagonal_moves():
            self._rotation.diagonal_rotate_right(self._ring_move_x, self._ring_move_y)
        elif (x, y) in self._possibles.get_left_diagonal_moves():
            self._rotation.diagonal_rotate_left(self._ring_move_x, self._ring_move_y)


        if self._player == 1:
            self._board.board[x][y] = 2
        else:
            self._board.board[x][y] = 3
        self._board.board[self._ring_move_x][self._ring_move_y] = self._player + 3

        return True


    def alignement(self):
        for i in range(11):
            for j in range(19):
                if self._board[i][j] > 3:
                    align = 1
                    for k in range(1, 5):
                        if self._board.board[i][j] == self._board.board[i][j+k*2]:
                            align += 1
                            if align == 5:
                                return True
                    align = 1
                    for k in range(1, 5):
                        if self._board.board[i][j] == self._board.board[i+k][j+k]:
                            align += 1
                            if align == 5:
                                return True
                    align = 1
                    for k in range(1, 5):
                        if self._board.board[i][j] == self._board.board[i-k][j+k]:
                            align += 1
                            if align == 5:
                                return True
        return False
