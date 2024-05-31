from tkinter import *


class Rings:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board
        self._player_1_out_ring = None
        self._player_2_out_ring = None

    def put_rings(self, x, y, board, player):
        """
        Use only in start of game, to put the first player's rings on the board.
        """
        self._x = x
        self._y = y

        if player == 1:
            self._board[self._x][self._y] = 2
        elif player == 2:
            self._board[self._x][self._y] = 3
        return board

    def alignement_1(self):
        for i in range(self.__n):
            for j in range(self.__n):
                if self.__plateau[i][j] > 2:
                    align = 1
                    for k in range(1, 6):
                        if i+k < self.__n :
                            if self.__plateau[i+2*k][j] == self.__plateau[i][j]:
                                align += 1
                                if align == 6:
                                    return True
                    align = 1
                    for k in range(1, 6):
                        if i+k < self.__n and j+k < self.__n:
                            if self.__plateau[i+k][j+k] == self.__plateau[i][j]:
                                align += 1
                                if align == 6:
                                    return True
                    align = 1
                    for k in range(1, 6):
                        if j+k < self.__n:
                            if self.__plateau[i][j+k] == self.__plateau[i][j]:
                                align += 1
                                if align == 6:
                                    return True
                    align = 1
                    for k in range(1, 6):
                        if i+k < self.__n and j-k > -1:
                            if self.__plateau[i+k][j-k] == self.__plateau[i][j]:
                                align += 1
                                if align == 6:
                                    return True
        return False

    def set_player_1_ring(self):
        """
        Use to count how many player 1 get out of the board.
        """
        self._player_1_out_ring = 0
        pass

    def get_player_1_ring(self):
        return self._player_1_out_ring

    def set_player_2_ring(self):
        """
        Use to count how many player 2 get out of the board.
        """
        self._player_2_out_ring = 0
        pass

    def get_player_2_ring(self):
        return self._player_2_out_ring
