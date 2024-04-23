from tkinter import *


class Rings:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board

    def possible_ring(self):
        if self._board[self._x][self._y] == 0:
            return False



    def put_rings(self, board):
        """
        Use only in start of game, to put the first player's rings on the board.
        :return: The complete board with the player's rings.
        """

        ring_round = 0

        while ring_round < 2 :
            print("Pion en placement : ", ring_round + 1)
            xring_player_1 = int(input("Player 1, (x) where do you want to put your ring? : "))
            yring_player_1 = int(input("Player 1, (y) where do you want to put your ring? : "))

            # Ces boucles vériient si les coordonnées sont valides (comprise dans le plateau mais aussi case vide)
            while self.board[0][0] <= xring_player_1 > len(self.board) or self.board[0][0] <= yring_player_1 > len(self.board) or self.board[xring_player_1][yring_player_1] != 1 :
                xring_player_1 = int(input("Player 1, invalid x ring : "))
                yring_player_1 = int(input("Player 1, invalid y ring : "))
            self.board[xring_player_1][yring_player_1] = 2  # Changer l'état de la case du plateau

            xring_player_2 = int(input("Player 2, (x) where do you want to put your ring? : "))
            yring_player_2 = int(input("Player 2, (y) where do you want to put your ring? : "))

            while self.board[0][0] <= xring_player_2 > len(self.board) or self.board[0][0] <= yring_player_2 > len(self.board) or self.board[xring_player_2][yring_player_2] != 1 :
                xring_player_2 = int(input("Player 2, invalid x ring? : "))
                yring_player_2 = int(input("Player 2, invalid y ring? : "))
            self.board[xring_player_2][yring_player_2] = 3  # Changer l'état de la case du plateau
            ring_round += 1

        return board