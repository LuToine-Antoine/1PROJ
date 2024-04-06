from structures.board.board_struct import *
from structures.board.board_ui import *

for i in range(11):
    for j in range(19):
        if board[i][j] == 0:
            print(" ", end='')
        else:
            print("o", end='')
    print(" ")
