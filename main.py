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
        self.all_possibles_moves = []
        self._possibles = RingsMoves(0, 0, self._board.board)


    def set_game_mode(self, mode=0):
        self._game_mode = mode

    def get_game_mode(self):
        return self._game_mode

    def get_board(self):
        return self._board.board

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

        if self._game_mode == False:
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

    def game_loop(self):
        """
        Use to run the game
        """
        self._game_mode = self.get_blitz_mode()
        self.main_put_first_rings()

        while not self.win():
            self.main_put_pawns()
            self.main_see_moves_rings()
            self.main_move_rings()
            self._board.see_board()
            self._round += 1
            if self._player == 1:
                self._player = 2
            else:
                self._player = 1

        # End of the game
        if self.win() == 1:
            print("Player 1 win")
        elif self.win() == 2:
            print("Player 2 win")
        else:
            print("Equality")

    def in_board_verification(self, x, y):
        """
        Use to check if the place selected is in the board
        """
        if 0 < x < 11 and 0 < y < 19:
            return True
        else:
            return False

    def main_put_first_rings(self):
        """
        Use to place 5 rings for each player at the start of the game
        """
        firstRing = Rings(0, 0, self._board.board)

        while self._round < 4:  #A CHANGER PLUS TARD C'EST JUSTE POUR LES TESTs !!!!!!!!!!!!!!!!!!!!!!!
            x = int(input(f"Player {self._player} : Set x for your ring : "))
            y = int(input(f"Player {self._player} : Set y for your ring : "))
            while not self.in_board_verification(x, y) or self._board.board[x][y] != 1:
                x = int(input(f"Player {self._player} : Not valid re-set x for your ring : "))
                y = int(input(f"Player {self._player} : Not valid re-set y for your ring : "))

            firstRing.put_rings(x, y, self._board.board, self._player)
            self._board.see_board()
            self._round += 1
            if self._player == 1:
                self._player = 2
            else:
                self._player = 1

    def main_put_pawns(self):
        """
        Use to place pawns on the board
        """
        pawns = Paws(0, 0, self._board.board)

        # In order to check if place selected is a ring of good player
        if self._player == 1:
            player_case = 2
        else:
            player_case = 3

        x = int(input(f"Player {self._player} : Set x for your pawn : "))
        y = int(input(f"Player {self._player} : Set y for your pawn : "))

        while not self.in_board_verification(x, y) or self._board.board[x][y] != player_case:
            x = int(input(f"Player {self._player} : Not valid re-set x for your pawn : "))
            y = int(input(f"Player {self._player} : Not valid re-set y for your pawn : "))

        pawns.put_paws(x, y, self._board.board, self._player)
        self._board.board[x][y] = self._player + 5
        self._board.see_board()

        # Use to check automaticaly ring's possibilities
        self._ring_move_x = x
        self._ring_move_y = y

        return self._ring_move_x, self._ring_move_y

    def main_see_moves_rings(self):
        """
        Check all possibles moves for rings where player has put his pawn
        """
        self.all_possibles_moves.clear()

        # Get all possibles moves
        self._possibles.get_possible_moves(self._ring_move_x, self._ring_move_y)
        if self._possibles.get_horizontal_moves() is None:
            self.main_put_pawns()

        # Create a list of all possibles moves
        self.all_possibles_moves =  self._possibles.get_horizontal_moves() + self._possibles.get_right_diagonal_moves() + self._possibles.get_left_diagonal_moves()
        print("Possible horizontal : ", self._possibles.get_horizontal_moves(), "Possible top left to bottom right : ", self._possibles.get_right_diagonal_moves(), "Possible bottom left to top right : ", self._possibles.get_left_diagonal_moves(), sep="\n")
        self._board.see_board()

        return self.all_possibles_moves

    def main_move_rings(self):
        """
        Use to choose ring's destination
        """
        self._rotation = PawnRotate(self._board.board)
        x = int(input(f"Player {self._player} : Set x for your destination rings : "))
        y = int(input(f"Player {self._player} : Set y for your destination rings : "))

        if self._player == 1:
            player_case = 2
        else:
            player_case = 3

        while not self.in_board_verification(x, y) or self._board.board[x][y] != 1 or (x,y) not in self.all_possibles_moves:
            x = int(input(f"Player {self._player} : Not valid re-set x for your destination rings : "))
            y = int(input(f"Player {self._player} : Not valid re-set y for your destination rings : "))

        if (x, y) in self._possibles.get_horizontal_moves():
            self._rotation.horizontal_rotate(self._ring_move_x, self._ring_move_y)
        elif (x, y) in self._possibles.get_right_diagonal_moves():
            self._rotation.right_diagonal_rotate(self._ring_move_x, self._ring_move_y)
        elif (x, y) in self._possibles.get_left_diagonal_moves():
            self._rotation.left_diagonal_rotate(self._ring_move_x, self._ring_move_y)

        self._board.board[x][y] = player_case
        self._board.board[self._ring_move_x][self._ring_move_y] = self._player + 3

    
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


game = Game()
game.game_loop()
