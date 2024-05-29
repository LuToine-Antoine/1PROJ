class RingsMoves:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board
        self._horizontal_moves = []
        self._right_diagonal_moves = []
        self._left_diagonal_moves = []

    
    def set_horizontal_moves(self):
        self._horizontal_moves.clear()
        for i in range(self._y + 1, len(self._board[self._x])):
            if self._board[self._x][i] == 4 or self._board[self._x][i] == 5:
                for i2 in range(self._y + 1, i):
                    if self._board[self._x][i2] == 1:
                        self._horizontal_moves.append((self._x, i2))
                if self._board[self._x][i + 2] != 1:
                    self._horizontal_moves.append((self._x, i + 2))
            elif self._board[self._x][i] == 2 or self._board[self._x][i] == 3:
                for i3 in range(self._y + 1, i):
                    if self._board[self._x][i3] == 1:
                        self._horizontal_moves.append((self._x, i3))
            else:
                if self._board[self._x][i] == 1:
                    self._horizontal_moves.append((self._x, i))
        for j in range(self._y - 1, -1, -1):
            if self._board[self._x][j] == 4 or self._board[self._x][j] == 5:
                for j2 in range(j + 1, self._y):
                    if self._board[self._x][j2] == 1:
                        self._horizontal_moves.append((self._x, j2))
                if self._board[self._x][j - 2] != 1:
                    self._horizontal_moves.append((self._x, j - 2))
            elif self._board[self._x][j] == 2 or self._board[self._x][j] == 3:
                for j3 in range(j + 1, self._y):
                    if self._board[self._x][j3] == 1:
                        self._horizontal_moves.append((self._x, j3))
            else:
                if self._board[self._x][j] == 1:
                    self._horizontal_moves.append((self._x, j))

    def set_diagonal_moves(self):
        self._right_diagonal_moves.clear()
        self._left_diagonal_moves.clear()
        
        # Scan top-right diagonal
        i, j = self._x - 1, self._y + 1
        while i >= 0 and j < len(self._board[0]):
            if self._board[self._x][i] == 4 or self._board[self._x][i] == 5:
                for k in range(1, min(self._x - i, j - self._y)):
                    if self._board[self._x - k][self._y + k] == 1:
                        self._right_diagonal_moves.append((self._x - k, self._y + k))
                if self._board[i + 2][j - 2] != 1:
                    self._right_diagonal_moves.append((i + 2, j - 2))
            elif self._board[self._x][i] == 2 or self._board[self._x][i] == 3:
                for k in range(1, min(self._x - i, j - self._y)):
                    if self._board[self._x - k][self._y + k] == 1:
                        self._right_diagonal_moves.append((self._x - k, self._y + k))
            else:
                if self._board[i][j] == 1:
                    self._right_diagonal_moves.append((i, j))
            i -= 1
            j += 1
        
        # Scan top-left diagonal
        i, j = self._x - 1, self._y - 1
        while i >= 0 and j >= 0:
            if self._board[self._x][i] == 4 or self._board[self._x][i] == 5:
                for k in range(1, min(self._x - i, self._y - j)):
                    if self._board[self._x - k][self._y - k] == 1:
                        self._left_diagonal_moves.append((self._x - k, self._y - k))
                if self._board[i + 2][j + 2] != 1:
                    self._left_diagonal_moves.append((i + 2, j + 2))
            elif self._board[self._x][i] == 2 or self._board[self._x][i] == 3:
                for k in range(1, min(self._x - i, self._y - j)):
                    if self._board[self._x - k][self._y - k] == 1:
                        self._left_diagonal_moves.append((self._x - k, self._y - k))
            else:
                if self._board[i][j] == 1:
                    self._left_diagonal_moves.append((i, j))
            i -= 1
            j -= 1
        
        # Scan bottom-right diagonal
        i, j = self._x + 1, self._y + 1
        while i < len(self._board) and j < len(self._board[0]):
            if self._board[self._x][i] == 4 or self._board[self._x][i] == 5:
                for k in range(1, min(i - self._x, j - self._y)):
                    if self._board[self._x + k][self._y + k] == 1:
                        self._right_diagonal_moves.append((self._x + k, self._y + k))
                if self._board[i - 2][j - 2] != 1:
                    self._right_diagonal_moves.append((i - 2, j - 2))
            elif self._board[self._x][i] == 2 or self._board[self._x][i] == 3:
                for k in range(1, min(i - self._x, j - self._y)):
                    if self._board[self._x + k][self._y + k] == 1:
                        self._right_diagonal_moves.append((self._x + k, self._y + k))
            else:
                if self._board[i][j] == 1:
                    self._right_diagonal_moves.append((i, j))
            i += 1
            j += 1
        
        # Scan bottom-left diagonal
        i, j = self._x + 1, self._y - 1
        while i < len(self._board) and j >= 0:
            if self._board[self._x][i] == 4 or self._board[self._x][i] == 5:
                for k in range(1, min(i - self._x, self._y - j)):
                    if self._board[self._x + k][self._y - k] == 1:
                        self._left_diagonal_moves.append((self._x + k, self._y - k))
                if self._board[i - 2][j + 2] != 1:
                    self._left_diagonal_moves.append((i - 2, j + 2))
            elif self._board[self._x][i] == 2 or self._board[self._x][i] == 3:
                for k in range(1, min(i - self._x, self._y - j)):
                    if self._board[self._x + k][self._y - k] == 1:
                        self._left_diagonal_moves.append((self._x + k, self._y - k))
            else:
                if self._board[i][j] == 1:
                    self._left_diagonal_moves.append((i, j))
            i += 1
            j -= 1

    def get_horizontal_moves(self):
        return self._horizontal_moves

    def set_diagonal_moves(self):
        self._right_diagonal_moves.clear()
        self._left_diagonal_moves.clear()

        directions = [(-1, 1), (-1, -1), (1, 1), (1, -1)]
        for direction in directions:
            i, j = self._x + direction[0], self._y + direction[1]
            moves_list = self._right_diagonal_moves if direction in [(-1, 1), (1, 1)] else self._left_diagonal_moves

            while 0 <= i < len(self._board) and 0 <= j < len(self._board[0]):
                if self._board[i][j] == 4 or self._board[i][j] == 5:
                    break
                elif self._board[i][j] == 2 or self._board[i][j] == 3:
                    i += direction[0]
                    j += direction[1]
                    continue
                elif self._board[i][j] == 1:
                    moves_list.append((i, j))
                    break
                i += direction[0]
                j += direction[1]

    def get_diagonal_moves(self):
        return self._right_diagonal_moves + self._left_diagonal_moves

    def get_possible_moves(self, x, y):
        self._x = x
        self._y = y
        self.set_horizontal_moves()
        self.set_diagonal_moves()
        return self.get_horizontal_moves(), self.get_diagonal_moves()
