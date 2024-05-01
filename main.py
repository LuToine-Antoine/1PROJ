import tkinter as tk

from structures.board.board_struct import *
from structures.board.board_ui import *
from structures.rings import *
from structures.pawn import *

class Menu:
    def __init__(self):
        self.mode = None

    def blitz_mode(self):
        '''
        True = blitz mode; False = normal mode
        '''
        setMode = int(input("Choose a mode : 1 for normal (3 for win) mode, 2 for blitz (1 for win) mode"))

        if setMode == 1:
            return False
        else:
            return True

    def game_loop(self):
        ui_board = UIBoard()

        board = BoardStruct()
        board.see_board()

        firstRing = Rings(0, 0, board.board)
        firstRing.put_rings(board.board)

        board.see_board()

        pawns = Paws(0, 0, board.board)
        pawns.put_paws(board.board)
        board.see_board()


    #ui_board.draw_triangles()


menu = Menu()
menu.game_loop()