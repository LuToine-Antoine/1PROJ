import tkinter as tk

from structures.board.board_struct import *
from structures.board.board_ui import *
from structures.rings import *
from structures.pawn import *
from possibilites.ringsmoves import *


class Menu:
    def __init__(self):
        self.mode = None

    def blitz_mode(self):
        '''
        True = blitz mode; False = normal mode
        '''
        setMode = int(input("Choose a mode : 1 for normal (3 for win) mode, 2 for blitz (1 for win) mode"))

        if setMode == 1:
            return False # Isn't blitz mode
        else:
            return True # It's blitz mode

    def win(self):
        '''
        Check if a player win
        '''
        board = BoardStruct()
        numberRing = Rings(0, 0, board.board)
        pawns = Paws(0, 0, board.board)
        pawnStock = pawns.pawns_stock(board.board)
        numberRingPlayer1 = numberRing.get_player_1_ring()
        numberRingPlayer2 = numberRing.get_player_2_ring()

        if self.mode == False:
            numberToWin = 3
        else:
            numberToWin = 1

        if numberRingPlayer1 == numberToWin:
            return 1 # Player 1 win
        elif numberRingPlayer2 == numberToWin:
            return 2 # Player 2 win
        elif pawnStock == True: # No pawns left
            if numberRingPlayer1 > numberRingPlayer2:
                return 1 # Player 1 win
            elif numberRingPlayer2 > numberRingPlayer1:
                return 2 # Player 2 win
            else:
                return 3  # Equality




    def game_loop(self):
        #ui_board = UIBoard()

        board = BoardStruct()
        board.see_board()

        possibles = RingsMoves(4, 8, board.board)
        firstRing = Rings(0, 0, board.board)
        firstRing.put_rings(board.board)
        possibles.set_vertical_moves()
        possibles.set_horizontal_moves()
        possibles.set_right_diagonal_moves()
        possibles.set_left_diagonal_moves()

        print(possibles.get_vertical_moves(), possibles.get_horizontal_moves(), possibles.get_right_diagonal_moves(), possibles.get_left_diagonal_moves(),  sep="\n")

        board.see_board()

       #pawns = Paws(0, 0, board.board)
       #pawns.put_paws(board.board)
        #board.see_board()


    #ui_board.draw_triangles()


menu = Menu()
menu.game_loop()