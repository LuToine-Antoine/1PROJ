from tkinter import *

class Paws:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board

    def pawns_stock(self, board):
        """
        Check if stock is empty or not
        """
        stock = 51

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 3 or board[i][j] == 4:
                    stock -= 1

        if stock != 0:
            return False  # Stock is not empty
        else:
            return True

    def put_paws(self, x, y, board, player):
        """
        Use for player to put their paws on the board.
        """
        self._x = x
        self._y = y

        if player == 1:
            self._board[self._x][self._y] = 4  # Changer l'état de la case du plateau
        elif player == 2:
            self._board[self._x][self._y] = 5  # Changer l'état de la case du plateau
        return board



