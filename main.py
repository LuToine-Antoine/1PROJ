import tkinter as tk

from structures.board.board_struct import *
from structures.board.board_ui import *
from structures.rings import *
from structures.pawn import *
from possibilites.ringsmoves import *


class Game:
    def __init__(self):
        self._mode = None
        self._round = 0
        self._player = 1
        self._ring_move_x = 0
        self._ring_move_y = 0
        self.all_possibles_moves = []

    def blitz_mode(self):
        """
        True = blitz mode; False = normal mode
        """
        setMode = int(input("Choose a mode : 1 for normal (3 for win) mode, 2 for blitz (1 for win) mode : "))

        if setMode == 1:
            self._mode = False  # Isn't blitz mode
        else:
            self._mode = True  # It's blitz mode

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

        if self._mode == False:
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
        #ui_board = UIBoard()

        self._board = BoardStruct()
        self._mode = self.blitz_mode()
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

    def in_board_verification(self, x, y):
        if 0 < x < 11 and 0 < y < 19:
            return True
        else:
            return False

    def main_put_first_rings(self):
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
        self._board.see_board()

        # Use to check automaticaly ring's possibilities
        self._ring_move_x = x
        self._ring_move_y = y

        return self._ring_move_x, self._ring_move_y

    def main_see_moves_rings(self):
        self.all_possibles_moves.clear()
        possibles = RingsMoves(0, 0, self._board.board)

        # Get all possibles moves
        possibles.get_possible_moves(self._ring_move_x, self._ring_move_y)

        # Create a list of all possibles moves
        self.all_possibles_moves = possibles.get_vertical_moves() + possibles.get_horizontal_moves() + possibles.get_right_diagonal_moves() + possibles.get_left_diagonal_moves()
        print("ring coordonnées", self._ring_move_x, self._ring_move_y)
        print("Possible vertical : ", possibles.get_vertical_moves(), "Possible horizontal : ", possibles.get_horizontal_moves(), "Possible top left to bottom right : ", possibles.get_right_diagonal_moves(), "Possible bottom left to top right : ", possibles.get_left_diagonal_moves(), sep="\n")
        self._board.see_board()

        return self.all_possibles_moves


    def main_move_rings(self):
        x = int(input(f"Player {self._player} : Set x for your destination rings : "))
        y = int(input(f"Player {self._player} : Set y for your destination rings : "))

        if self._player == 1:
            player_case = 2
        else:
            player_case = 3

        print("all_possibles_moves", self.all_possibles_moves)

        while not self.in_board_verification(x, y) or self._board.board[x][y] != 1 or (x,y) not in self.all_possibles_moves:
            # dev tests
            if self._board.board[x][y] not in self.all_possibles_moves:
                print("Not a valid move")

            elif not self.in_board_verification(x, y):
                print("Not in board")

            elif self._board.board[x][y] != 1:
                print("Not 1")

            x = int(input(f"Player {self._player} : Not valid re-set x for your destination rings : "))
            y = int(input(f"Player {self._player} : Not valid re-set y for your destination rings : "))

        self._board.board[x][y] = player_case


game = Game()
game.game_loop()