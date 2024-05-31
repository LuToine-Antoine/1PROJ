class RingsMoves:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board
        self._vertical_moves = []
        self._right_diagonal_moves = []
        self._left_diagonal_moves = []

    def set_vertical_moves(self):
        self._vertical_moves.clear()
        upobstacle = False
        downobstacle = False
        for o in range(self._x + 1, len(self._board)):
            if self._board[o][self._y] in [2, 3, 4, 5]:
                upobstacle = True
        if upobstacle == True:
            for i in range(self._x + 1, len(self._board)):
                if self._board[i][self._y] in [4, 5]:
                    for i2 in range(self._x + 1, i):
                        if self._board[i2][self._y] == 1:
                            self._vertical_moves.append((i2, self._y))
                    if i + 2 < len(self._board) and self._board[i + 2][self._y] == 1:
                        self._vertical_moves.append((i + 2, self._y))
                        break
                elif self._board[i][self._y] in [2, 3]:
                    for i3 in range(self._x + 1, i):
                        if self._board[i3][self._y] == 1:
                            self._vertical_moves.append((i3, self._y))
        else:
            for i in range(self._x + 1, len(self._board)):
                if self._board[i][self._y] == 1:
                    self._vertical_moves.append((i, self._y))
        for o2 in range(self._x - 1, -1, -1):
            if self._board[o2][self._y] in [2, 3, 4, 5]:
                downobstacle = True
        if downobstacle == True:
            for j in range(self._x - 1, -1, -1):
                if self._board[j][self._y] in [4, 5]:
                    for j2 in range(j + 1, self._x):
                        if self._board[j2][self._y] == 1:
                            self._vertical_moves.append((j2, self._y))
                    if j - 2 >= 0 and self._board[j - 2][self._y] == 1:
                        self._vertical_moves.append((j - 2, self._y))
                        break
                elif self._board[j][self._y] in [2, 3]:
                    for j3 in range(j + 1, self._x):
                        if self._board[j3][self._y] == 1:
                            self._vertical_moves.append((j3, self._y))
        else:
            for j in range(self._x - 1, -1, -1):
                if self._board[j][self._y] == 1:
                    self._vertical_moves.append((j, self._y))

    def get_vertical_moves(self):
        return self._vertical_moves

    def set_diagonal_moves(self):
        self._right_diagonal_moves.clear()
        self._left_diagonal_moves.clear()
        up_left = []
        up_right = []
        down_left = []
        down_right = []

        up_right_obstacle = False
        for o in range(1, min(self._x + 1, len(self._board[0]) - self._y)):
            if self._board[self._x - o][self._y + o] in [2, 3, 4, 5]:
                up_right_obstacle = True
                break
        if up_right_obstacle:
            for i in range(1, min(self._x + 1, len(self._board[0]) - self._y)):
                if self._board[self._x - i][self._y + i] in [4, 5]:
                    for i2 in range(1, i):
                        if self._board[self._x - i2][self._y + i2] == 1:
                            up_right.append((self._x - i2, self._y + i2))
                    if self._x - i - 2 >= 0 and self._y + i + 2 < len(self._board[0]) and self._board[self._x - i - 2][self._y + i + 2] == 1 and not self._board[self._x - i - 2][self._y + i + 2] == [2,3,4,5]:
                        up_right.append((self._x - i - 2, self._y + i + 2))
                        break
                elif self._board[self._x - i][self._y + i] in [2, 3]:
                    for i3 in range(1, i):
                        if self._board[self._x - i3][self._y + i3] == 1:
                            up_right.append((self._x - i3, self._y + i3))
        else:
            for i in range(1, min(self._x + 1, len(self._board[0]) - self._y)):
                if self._board[self._x - i][self._y + i] == 1:
                    up_right.append((self._x - i, self._y + i))

        up_left_obstacle = False
        for o in range(1, min(self._x + 1, self._y + 1)):
            if self._board[self._x - o][self._y - o] in [2, 3, 4, 5]:
                up_left_obstacle = True
                break
        if up_left_obstacle:
            for i in range(1, min(self._x + 1, self._y + 1)):
                if self._board[self._x - i][self._y - i] in [4, 5]:
                    for i2 in range(1, i):
                        if self._board[self._x - i2][self._y - i2] == 1:
                            up_left.append((self._x - i2, self._y - i2))
                    if self._x - i - 2 >= 0 and self._y - i - 2 >= 0 and self._board[self._x - i - 2][self._y - i - 2] == 1 and not self._board[self._x - i - 2][self._y - i - 2] == [2,3,4,5]:
                        up_left.append((self._x - i - 2, self._y - i - 2))
                        break
                elif self._board[self._x - i][self._y - i] in [2, 3]:
                    for i3 in range(1, i):
                        if self._board[self._x - i3][self._y - i3] == 1:
                            up_left.append((self._x - i3, self._y - i3))
        else:
            for i in range(1, min(self._x + 1, self._y + 1)):
                if self._board[self._x - i][self._y - i] == 1:
                    up_left.append((self._x - i, self._y - i))

        down_right_obstacle = False
        for o in range(1, min(len(self._board) - self._x, len(self._board[0]) - self._y)):
            if self._board[self._x + o][self._y + o] in [2, 3, 4, 5]:
                down_right_obstacle = True
                break
        if down_right_obstacle:
            for i in range(1, min(len(self._board) - self._x, len(self._board[0]) - self._y)):
                if self._board[self._x + i][self._y + i] in [4, 5]:
                    for i2 in range(1, i):
                        if self._board[self._x + i2][self._y + i2] == 1:
                            self._right_diagonal_moves.append((self._x + i2, self._y + i2))
                    if self._x + i + 2 < len(self._board) and self._y + i + 2 < len(self._board[0]) and self._board[self._x + i + 2][self._y + i + 2] == 1 and not self._board[self._x + i + 2][self._y + i + 2] == [2,3,4,5]:
                        self._right_diagonal_moves.append((self._x + i + 2, self._y + i + 2))
                        break
                elif self._board[self._x + i][self._y + i] in [2, 3]:
                    for i3 in range(1, i):
                        if self._board[self._x + i3][self._y + i3] == 1:
                            self._right_diagonal_moves.append((self._x + i3, self._y + i3))
        else:
            for i in range(1, min(len(self._board) - self._x, len(self._board[0]) - self._y)):
                if self._board[self._x + i][self._y + i] == 1:
                    self._right_diagonal_moves.append((self._x + i, self._y + i))

        down_left_obstacle = False
        for o in range(1, min(len(self._board) - self._x, self._y + 1)):
            if self._board[self._x + o][self._y - o] in [2, 3, 4, 5]:
                down_left_obstacle = True
                break
        if down_left_obstacle:
            for i in range(1, min(len(self._board) - self._x, self._y + 1)):
                if self._board[self._x + i][self._y - i] in [4, 5]:
                    for i2 in range(1, i):
                        if self._board[self._x + i2][self._y - i2] == 1:
                            self._left_diagonal_moves.append((self._x + i2, self._y - i2))
                    if self._x + i + 2 < len(self._board) and self._y - i - 2 >= 0 and self._board[self._x + i + 2][self._y - i - 2] == 1 and not self._board[self._x + i + 2][self._y - i - 2] == [2,3,4,5]:
                        self._left_diagonal_moves.append((self._x + i + 2, self._y - i - 2))
                        break
                elif self._board[self._x + i][self._y - i] in [2, 3]:
                    for i3 in range(1, i):
                        if self._board[self._x + i3][self._y - i3] == 1:
                            self._left_diagonal_moves.append((self._x + i3, self._y - i3))
        else:
            for i in range(1, min(len(self._board) - self._x, self._y + 1)):
                if self._board[self._x + i][self._y - i] == 1:
                    self._left_diagonal_moves.append((self._x + i, self._y - i))

    def get_right_diagonal_moves(self):
        return self._right_diagonal_moves

    def get_left_diagonal_moves(self):
        return self._left_diagonal_moves

    def get_diagonal_moves(self):
        return self._right_diagonal_moves + self._left_diagonal_moves

    def get_possible_moves(self, x, y):
        self._x = x
        self._y = y
        self.set_vertical_moves()
        self.set_diagonal_moves()
        return self.get_vertical_moves(), self.get_diagonal_moves()

#    def set_diagonal_moves(self):
 #       self._vertical_moves.clear()
  #      up_right_obstacle = False
   #     for o in range(1, min(self._x + 1, len(self._board[0]) - self._y)):
    #        if self._board[self._x - o][self._y + o] in [2, 3, 4, 5]:
     #           up_right_obstacle = True
      #  if up_right_obstacle == True:
       #     for i in range(self._x + 1, len(self._board)):
        #        if self._board[self._x - i][self._y + i] in [4, 5]:
         #           for i2 in range(self._y + 1, i):
          #              if self._board[self._x - i2][self._y + i2] == 1:
           #                 self._diagonal_moves.append((i2, i2))
            #        if self._x - i - 2 >= 0 and self._y + i + 2 < len(self._board[0]) and self._board[self._x - i - 2][self._y + i + 2] == 1:
             #           self._vertical_moves.append((i+2, i+2))
              #          break
               # elif self._board[i][self._y] in [2, 3]:
                #    for i3 in range(self._x + 1, i):
                 #       if self._board[i3][self._y] == 1:
                  #          self._vertical_moves.append((i3, self._y))
#        else:
 #           for i in range(self._x + 1, len(self._board)):
  #              if self._board[i][self._y] == 1:
   #                 self._vertical_moves.append((i, self._y))