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

    def put_paws(self, board):
        """
        Use for player to put their paws on the board.
        """
        # Set to default
        xpawn_player_1 = 0
        ypawn_player_1 = 0
        xpawn_player_2 = 0
        ypawn_player_2 = 0
        pawn_round = 0

        #while self.pawns_stock(board) == False:
        while pawn_round < 2:
            print("Tour = : ", pawn_round)
            while not (0 < xpawn_player_1 < 11) or not (0 < ypawn_player_1 < 19) or self._board[xpawn_player_1][ypawn_player_1] != 2:
                xpawn_player_1 = int(input("Player 1, set x for your pawn : "))
                ypawn_player_1 = int(input("Player 1, set y for your pawn : "))
            self._board[xpawn_player_1][ypawn_player_1] = 4  # Changer l'état de la case du plateau

            while not (0 < xpawn_player_2 < 11) or not (0 < ypawn_player_2 < 19) or self._board[xpawn_player_2][ypawn_player_2] != 3:
                xpawn_player_2 = int(input("Player 2, set x for your pawn : "))
                ypawn_player_2 = int(input("Player 2, set y for your pawn : "))
            self._board[xpawn_player_2][ypawn_player_2] = 5  # Changer l'état de la case du plateau

            pawn_round += 1

