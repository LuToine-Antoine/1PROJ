from tkinter import *


class Rings:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board

    def put_rings(self, board):
        """
        Use only in start of game, to put the first player's rings on the board.
        """
        # Set to default
        xring_player_1 = 0
        yring_player_1 = 0
        xring_player_2 = 0
        yring_player_2 = 0
        ring_round = 0

        while ring_round < 2:
            print("Pion en placement : ", ring_round + 1)

            # Ces boucles vériient si les coordonnées sont valides (comprise dans le plateau mais aussi case vide)
            while self._board[0][0] <= xring_player_1 > len(self._board) or self._board[0][0] <= yring_player_1 > len(self._board) or self._board[xring_player_1][yring_player_1] != 1 :
                xring_player_1 = int(input("Player 1, set x for your ring : "))
                yring_player_1 = int(input("Player 1, set y for your ring : "))
            self._board[xring_player_1][yring_player_1] = 2  # Changer l'état de la case du plateau

            while self._board[0][0] <= xring_player_2 > len(self._board) or self._board[0][0] <= yring_player_2 > len(self._board) or self._board[xring_player_2][yring_player_2] != 1 :
                xring_player_2 = int(input("Player 2, set x for your ring : "))
                yring_player_2 = int(input("Player 2, set y for your ring : "))
            self._board[xring_player_2][yring_player_2] = 3  # Changer l'état de la case du plateau
            ring_round += 1

        return board