from tkinter import *

class Paws:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board
        self._stock = None

    def empty_stock(self, board):
        """
        Check if stock is empty or not
        """
        stock = 51

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 4 or board[i][j] == 5:
                    stock -= 1

        self._stock = stock
        if stock == 0:
            return True # Stock is empty
        print(stock, "stcok pawn fichier")

    def get_stock(self):
        return self._stock

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



