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
        self._solo_mode = 0
        self._change_player = True
        self._player_1_out_ring = 0
        self._player_2_out_ring = 0
        self._player_1_align = 0
        self._player_2_align = 0
        self._board = BoardStruct()
        self._round = 0
        self._player = 1
        self._ring_move_x = 0
        self._ring_move_y = 0
        self._clickCount = 0
        self.all_possibles_moves = []
        self._choix = []
        self._pawns = Paws(0, 0, self._board.board)
        self._possibles = RingsMoves(0, 0, self._board.board)
        self._firstRing = Rings(0, 0, self._board.board)
        self._pawnStock = False
        self._click_x = None
        self._click_y = None

    def get_pawn(self):
        return self._pawns

    def set_game_mode(self, mode=1):
        self._game_mode = mode

    def set_solo_mode(self):
        if self._solo_mode == 1:
            return True
        elif self._solo_mode == 2:
            return False

    def get_game_mode(self):
        return self._game_mode

    def get_board(self):
        return self._board.board

    def reset_board(self):
        for i in range(len(self._board.board)):
            for j in range(len(self._board.board[0])):
                if self._board.board[i][j] not in (0, 1):
                    self._board.board[i][j] = 1
        return self._board.board

    def get_player(self):
        return self._player

    def get_turn(self):
        return self._round

    def reset_turn(self):
        self._round = 0

    def get_possible(self):
        return self._possibles

    def get_ring_player_1(self):
        return self._player_1_out_ring

    def get_ring_player_2(self):
        return self._player_2_out_ring

    def reset_player_rings(self):
        self._player_1_out_ring = 0
        self._player_2_out_ring = 0

    def set_blitz_mode(self, mode=0):
        """
        True = blitz mode; False = normal mode
        """
        if mode == 1:
            self._mode = False  # Isn't blitz mode
        else:
            self._mode = True  # It's blitz mode

    def get_blitz_mode(self):
        return self._mode

    def win(self):
        """
        Check if a player win
        """
        board = BoardStruct()
        numberRingPlayer1 = self._player_1_out_ring
        numberRingPlayer2 = self._player_2_out_ring
        self._pawnStock = self._pawns.get_stock()

        if not self._mode:
            numberToWin = 3
        else:
            numberToWin = 1

        # Check if a player win with check order by player turn
        if self._round % 2 == 0:  # Check win during player 1 turn
            if numberRingPlayer1 == numberToWin:
                return 1  # Player 1 win
            elif numberRingPlayer2 == numberToWin:
                return 2  # Player 2 win
            elif self._pawnStock:  # No pawns left
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
            elif self._pawnStock:  # No pawns left
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
            if self._player == 1:
                caseplayer = 2
            else:
                caseplayer = 3

            if self._round < 10:
                self.main_put_first_rings(self._click_x, self._click_y)

            # Check if a player can remove a ring and add ring in his ring out stock
            self.alignement()
            if self._player_1_align > self._player_1_out_ring:
                self.choix_anneaux(1)
                if (self._click_x, self._click_y) in self._choix:
                    self.ring_out(self._click_x, self._click_y, 1)
                self._player = 2

            elif self._player_2_align > self._player_2_out_ring:
                self.choix_anneaux(2)
                if (self._click_x, self._click_y) in self._choix:
                    self.ring_out(self._click_x, self._click_y, 2)
                self._player = 1

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

        self._pawns.empty_stock(self._board.board)
        print(self._pawnStock)

        print(self._player_1_out_ring, self._player_2_out_ring)

    def get_click_count(self):
        return self._clickCount

    def ring_out(self, x, y, player):
        """
        Use to remove rings from the board
        """
        if player == 1:
            self._player_1_out_ring += 1
        else:
            self._player_2_out_ring += 1

        self._board.board[x][y] = 1

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

        return self.all_possibles_moves

    def main_move_rings(self, x, y, player):
        """
        Use to choose ring's destination
        """
        self._rotation = PawnRotate(self._board.board)

        if not self.in_board_verification(x, y) or self._board.board[x][y] != 1 or (x,y) not in self.all_possibles_moves:
            return False

        print(x, y, self._possibles.get_vertical_moves())

        if (x, y) in self._possibles.get_vertical_moves():
            self._rotation.vertical_rotate(self._ring_move_y, self._ring_move_x, x)

        elif (x, y) in self._possibles.get_up_right_diagonal_moves():
            self._rotation.diagonal_rotate_up_right(self._ring_move_y, self._ring_move_x, y, x)

        elif (x, y) in self._possibles.get_up_left_diagonal_moves():
            self._rotation.diagonal_rotate_up_left(self._ring_move_y, self._ring_move_x, y, x)

        elif (x, y) in self._possibles.get_down_right_diagonal_moves():
            self._rotation.diagonal_rotate_down_right(self._ring_move_y, self._ring_move_x, y, x)

        elif (x, y) in self._possibles.get_down_left_diagonal_moves():
            self._rotation.diagonal_rotate_down_left(self._ring_move_y, self._ring_move_x, y, x)

        if self._player == 1:
            self._board.board[x][y] = 2
        else:
            self._board.board[x][y] = 3
        self._board.board[self._ring_move_x][self._ring_move_y] = self._player + 3

        return True

    def alignement(self):
        for i in range(19):
            for j in range(11):
                if self._board.board[i][j] == 4:
                    align = 1
                    for k in range(1, 5):
                        if i+k < 19 and j+k < 11:
                            if self._board.board[i+k][j+k] == self._board.board[i][j]:
                                align += 1
                                if align == 5:
                                    self._board.board[i][j], self._board.board[i+1][j+1], self._board.board[i+2][j+2], self._board.board[i+3][j+3], self._board.board[i+4][j+4] = 1, 1, 1, 1, 1
                                    self._player_1_align += 1
                                    return 1
                    align = 1
                    for k in range(1, 5):
                        if i+k*2 < 19:
                            if self._board.board[i+2*k][j] == self._board.board[i][j]:
                                align += 1
                                if align == 5:
                                    self._board.board[i][j], self._board.board[i+2][j], self._board.board[i+4][j], self._board.board[i+6][j], self._board.board[i+8][j] = 1, 1, 1, 1, 1
                                    self._player_1_align += 1
                                    return 1
                    align = 1
                    for k in range(1, 5):
                        if i-k >= 0 and j+k < 11:
                            if self._board.board[i-k][j+k] == self._board.board[i][j]:
                                align += 1
                                if align == 5:
                                    self._board.board[i][j], self._board.board[i-1][j+1], self._board.board[i-2][j+2], self._board.board[i-3][j+3], self._board.board[i-4][j+4] = 1, 1, 1, 1, 1
                                    self._player_1_align += 1
                                    return 1
                elif self._board.board[i][j] == 5:
                    align = 1
                    for k in range(1, 5):
                        if i+k < 19 and j+k < 11:
                            if self._board.board[i+k][j+k] == self._board.board[i][j]:
                                align += 1
                                if align == 5:
                                    self._board.board[i][j], self._board.board[i+1][j+1], self._board.board[i+2][j+2], self._board.board[i+3][j+3], self._board.board[i+4][j+4] = 1, 1, 1, 1, 1
                                    self._player_2_align += 1
                                    return 2
                    align = 1
                    for k in range(1, 5):
                        if i+k*2 < 19:
                            if self._board.board[i+2*k][j] == self._board.board[i][j]:
                                align += 1
                                if align == 5:
                                    self._board.board[i][j], self._board.board[i+2][j], self._board.board[i+4][j], self._board.board[i+6][j], self._board.board[i+8][j] = 1, 1, 1, 1, 1
                                    self._player_2_align += 1
                                    return 2
                    align = 1
                    for k in range(1, 5):
                        if i-k >= 0 and j+k < 11:
                            if self._board.board[i-k][j+k] == self._board.board[i][j]:
                                align += 1
                                if align == 5:
                                    self._board.board[i][j], self._board.board[i-1][j+1], self._board.board[i-2][j+2], self._board.board[i-3][j+3], self._board.board[i-4][j+4] = 1, 1, 1, 1, 1
                                    self._player_2_align += 1
                                    return 2
        return False

    def choix_anneaux(self, player):
        self._choix.clear()
        if player == 1:
            for i in range(19):
                for j in range(11):
                    if self._board.board[i][j] == 2:
                        self._choix.append((i,j))
            return self._choix
        if player == 2:
            for i in range(19):
                for j in range(11):
                    if self._board.board[i][j] == 3:
                        self._choix.append((i,j))
            return self._choix
    
    def get_player_1_ring(self):
        return self._player_1_out_ring

    def get_player_2_ring(self):
        return self._player_2_out_ring

    def ia_moves(self):
        if self.get_turn() > 10:
            all_moves = self._possibles.get_vertical_moves() + self._possibles.get_diagonal_moves()
            ia = randint(0, len(all_moves)-1)
            return all_moves[ia]
        else:
            rand_x = 0
            rand_y = 0
            while self._board.board[rand_x][rand_y] != 1:
                rand_x = randint(0, len(self._board.board)-1)
                rand_y = randint(0, len(self._board.board[0])-1)
            return rand_x, rand_y
