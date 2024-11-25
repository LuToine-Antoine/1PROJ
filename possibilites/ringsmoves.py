from random import *

class RingsMoves:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board
        self._vertical_moves = []
        self._up_right_diagonal_moves = []
        self._up_left_diagonal_moves = []
        self._down_right_diagonal_moves = []
        self._down_left_diagonal_moves = []

    def set_vertical_moves(self):
        self._vertical_moves.clear() #clear vertical moves list
        upobstacle = False 
        downobstacle = False #set obtacles on 0
        for o in range(self._x + 1, len(self._board)):
            if self._board[o][self._y] in [2, 3, 4, 5]:
                upobstacle = True #if there is a pawn or a ring, set obstacle on 1

        if upobstacle == True:
            for i in range(self._x + 1, len(self._board)):
                if self._board[i][self._y] in [4, 5]:
                    for i2 in range(self._x + 1, i):
                        if self._board[i2][self._y] == 1:
                            self._vertical_moves.append((i2, self._y)) 
                    if i + 2 < len(self._board) and self._board[i + 2][self._y] == 1 and not self._board[i + 2][self._y] == [2,3,4,5]:
                        self._vertical_moves.append((i + 2, self._y))
                        break #if there are some pawns as obstacles, stop at the case behind the pawn is it's not a pawn or a ring

                elif self._board[i][self._y] in [2, 3]:
                    for i3 in range(self._x + 1, i):
                        if self._board[i3][self._y] == 1:
                            self._vertical_moves.append((i3, self._y)) #if there are some rings as obstacles, stop at the case before the ring

        else:
            for i in range(self._x + 1, len(self._board)):
                if self._board[i][self._y] == 1:
                    self._vertical_moves.append((i, self._y)) #if there are not any obstalce, just append all moves

        for o2 in range(self._x - 1, -1, -1):
            if self._board[o2][self._y] in [2, 3, 4, 5]:
                downobstacle = True #if there is a pawn or a ring, set obstacle on 1

        if downobstacle == True:
            for j in range(self._x - 1, -1, -1):
                if self._board[j][self._y] in [4, 5]:
                    for j2 in range(j + 1, self._x):
                        if self._board[j2][self._y] == 1:
                            self._vertical_moves.append((j2, self._y))
                    if j - 2 >= 0 and self._board[j - 2][self._y] == 1 and not self._board[j - 2][self._y] == [2,3,4,5]:
                        self._vertical_moves.append((j - 2, self._y))
                        break #if there are some pawns as obstacles, stop at the case behind the pawn is it's not a pawn or a ring

                elif self._board[j][self._y] in [2, 3]:
                    for j3 in range(j + 1, self._x):
                        if self._board[j3][self._y] == 1:
                            self._vertical_moves.append((j3, self._y))#if there are some rings as obstacles, stop at the case before the ring
                            
        else:
            for j in range(self._x - 1, -1, -1):
                if self._board[j][self._y] == 1:
                    self._vertical_moves.append((j, self._y)) #if there are not any obstalce, just append all moves

    def get_vertical_moves(self):
        #return all vertical moves
        return self._vertical_moves

    def set_diagonal_moves(self):
        self._up_right_diagonal_moves.clear()
        self._up_left_diagonal_moves.clear()
        self._down_right_diagonal_moves.clear()
        self._down_left_diagonal_moves.clear() #clear all diagonal moves list

        up_right_obstacle = False #set obtacles on 0
        for o in range(1, min(self._x + 1, len(self._board[0]) - self._y)):
            if self._board[self._x - o][self._y + o] in [2, 3, 4, 5]:
                up_right_obstacle = True #if there is a pawn or a ring, set obstacle on 1
                break

        if up_right_obstacle:
            for i in range(1, min(self._x + 1, len(self._board[0]) - self._y)):
                if self._board[self._x - i][self._y + i] in [4, 5]:
                    for i2 in range(1, i):
                        if self._board[self._x - i2][self._y + i2] == 1:
                            self._up_right_diagonal_moves.append((self._x - i2, self._y + i2))
                    if self._x - i - 1 >= 0 and self._y + i + 1 < len(self._board[0]) and self._board[self._x - i - 1][self._y + i + 1] == 1 and not self._board[self._x - i - 1][self._y + i + 1] == [2,3,4,5]:
                        self._up_right_diagonal_moves.append((self._x - i - 1, self._y + i + 1))
                        break #if there are some pawns as obstacles, stop at the case behind the pawn is it's not a pawn or a ring

                elif self._board[self._x - i][self._y + i] in [2, 3]:
                    for i3 in range(1, i):
                        if self._board[self._x - i3][self._y + i3] == 1:
                            self._up_right_diagonal_moves.append((self._x - i3, self._y + i3)) #if there are some rings as obstacles, stop at the case before the ring

        else:
            for i in range(1, min(self._x + 1, len(self._board[0]) - self._y)):
                if self._board[self._x - i][self._y + i] == 1:
                    self._up_right_diagonal_moves.append((self._x - i, self._y + i)) #if there are not any obstalce, just append all moves

        up_left_obstacle = False #set obtacles on 0
        for o in range(1, min(self._x + 1, self._y + 1)):
            if self._board[self._x - o][self._y - o] in [2, 3, 4, 5]:
                up_left_obstacle = True #if there is a pawn or a ring, set obstacle on 1
                break

        if up_left_obstacle:
            for i in range(1, min(self._x + 1, self._y + 1)):
                if self._board[self._x - i][self._y - i] in [4, 5]:
                    for i2 in range(1, i):
                        if self._board[self._x - i2][self._y - i2] == 1:
                            self._up_left_diagonal_moves.append((self._x - i2, self._y - i2))
                    if self._x - i - 1 >= 0 and self._y - i - 1 >= 0 and self._board[self._x - i - 1][self._y - i - 1] == 1 and not self._board[self._x - i - 1][self._y - i - 1] == [2,3,4,5]:
                        self._up_left_diagonal_moves.append((self._x - i - 1, self._y - i - 1))
                        break #if there are some pawns as obstacles, stop at the case behind the pawn is it's not a pawn or a ring

                elif self._board[self._x - i][self._y - i] in [2, 3]:
                    for i3 in range(1, i):
                        if self._board[self._x - i3][self._y - i3] == 1:
                            self._up_left_diagonal_moves.append((self._x - i3, self._y - i3)) #if there are some rings as obstacles, stop at the case before the ring

        else:
            for i in range(1, min(self._x + 1, self._y + 1)):
                if self._board[self._x - i][self._y - i] == 1:
                    self._up_left_diagonal_moves.append((self._x - i, self._y - i)) #if there are not any obstalce, just append all moves

        down_right_obstacle = False #set obtacles on 0
        for o in range(1, min(len(self._board) - self._x, len(self._board[0]) - self._y)):
            if self._board[self._x + o][self._y + o] in [2, 3, 4, 5]:
                down_right_obstacle = True #if there is a pawn or a ring, set obstacle on 1
                break

        if down_right_obstacle:
            for i in range(1, min(len(self._board) - self._x, len(self._board[0]) - self._y)):
                if self._board[self._x + i][self._y + i] in [4, 5]:
                    for i2 in range(1, i):
                        if self._board[self._x + i2][self._y + i2] == 1:
                            self._down_right_diagonal_moves.append((self._x + i2, self._y + i2))
                    if self._x + i + 1 < len(self._board) and self._y + i + 1 < len(self._board[0]) and self._board[self._x + i + 1][self._y + i + 1] == 1 and not self._board[self._x + i + 1][self._y + i + 1] == [2,3,4,5]:
                        self._down_right_diagonal_moves.append((self._x + i + 1, self._y + i + 1))
                        break #if there are some pawns as obstacles, stop at the case behind the pawn is it's not a pawn or a ring

                elif self._board[self._x + i][self._y + i] in [2, 3]:
                    for i3 in range(1, i):
                        if self._board[self._x + i3][self._y + i3] == 1:
                            self._down_right_diagonal_moves.append((self._x + i3, self._y + i3)) #if there are some rings as obstacles, stop at the case before the ring

        else:
            for i in range(1, min(len(self._board) - self._x, len(self._board[0]) - self._y)):
                if self._board[self._x + i][self._y + i] == 1:
                    self._down_right_diagonal_moves.append((self._x + i, self._y + i)) #if there are not any obstalce, just append all moves

        down_left_obstacle = False #set obtacles on 0
        for o in range(1, min(len(self._board) - self._x, self._y + 1)):
            if self._board[self._x + o][self._y - o] in [2, 3, 4, 5]:
                down_left_obstacle = True #if there is a pawn or a ring, set obstacle on 1
                break

        if down_left_obstacle:
            for i in range(1, min(len(self._board) - self._x, self._y + 1)):
                if self._board[self._x + i][self._y - i] in [4, 5]:
                    for i2 in range(1, i):
                        if self._board[self._x + i2][self._y - i2] == 1:
                            self._down_left_diagonal_moves.append((self._x + i2, self._y - i2))
                    if self._x + i + 1 < len(self._board) and self._y - i - 1 >= 0 and self._board[self._x + i + 1][self._y - i - 1] == 1 and not self._board[self._x + i + 1][self._y - i - 1] == [2,3,4,5]:
                        self._down_left_diagonal_moves.append((self._x + i + 1, self._y - i - 1))
                        break #if there are some pawns as obstacles, stop at the case behind the pawn is it's not a pawn or a ring

                elif self._board[self._x + i][self._y - i] in [2, 3]:
                    for i3 in range(1, i):
                        if self._board[self._x + i3][self._y - i3] == 1:
                            self._down_left_diagonal_moves.append((self._x + i3, self._y - i3)) #if there are some rings as obstacles, stop at the case before the ring

        else:
            for i in range(1, min(len(self._board) - self._x, self._y + 1)):
                if self._board[self._x + i][self._y - i] == 1:
                    self._down_left_diagonal_moves.append((self._x + i, self._y - i)) #if there are not any obstalce, just append all moves

    def get_up_right_diagonal_moves(self):
        #return all up right moves
        return self._up_right_diagonal_moves

    def get_up_left_diagonal_moves(self):
        #return all up left moves
        return self._up_left_diagonal_moves

    def get_down_right_diagonal_moves(self):
        #return all down right moves
        return self._down_right_diagonal_moves

    def get_down_left_diagonal_moves(self):
        #return all down left moves
        return self._down_left_diagonal_moves

    def get_diagonal_moves(self):
        #return all diagonal moves
        return self._up_right_diagonal_moves + self._up_left_diagonal_moves + self._down_right_diagonal_moves + self._down_left_diagonal_moves

    def get_possible_moves(self, x, y):
        #return all possible moves
        self._x = x
        self._y = y
        self.set_vertical_moves()
        self.set_diagonal_moves()
        return self.get_vertical_moves(), self.get_diagonal_moves()
