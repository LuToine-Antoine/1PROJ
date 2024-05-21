class RingsMoves:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board
        self._vertical_moves = []
        self._horizontal_moves = []
        self._right_diagonal_moves = []
        self._left_diagonal_moves = []

    def set_vertical_moves(self):
        """
        Return a list of possibles vertical moves:
        """
        self._vertical_moves.clear()
        for i in range(len(self._board)):
            if self._board[i][self._y] == 1:
                if self._board[i][self._y] == 4 and self._board[i][self._y] == 5:  # Check if it's a pawn or not
                    self._vertical_moves.append((i+1, self._y+1))
                    break
                self._vertical_moves.append((i, self._y))

    def get_vertical_moves(self):
        return self._vertical_moves

    def set_horizontal_moves(self):
        self._horizontal_moves.clear()
        for j in range(len(self._board[self._x])):
            if self._board[self._x][j] == 4 and self._board[self._x][j] == 5:
                self._horizontal_moves.append((j+1, self._x+1))
                break
            if self._board[self._x][j] == 1:
                self._horizontal_moves.append((self._x, j))

    def get_horizontal_moves(self):
        return self._horizontal_moves

    def set_right_diagonal_moves(self):
        self._right_diagonal_moves.clear()
        min_left = min(self._x + 1, self._y + 1)  # For no out of range
        for i in range(1, min_left):
            if self._x - i < len(self._board) and self._y - i < len(self._board[0]) and self._board[self._x - i][self._y - i] == 1:
                self._right_diagonal_moves.append((self._x - i, self._y - i))

        max_right = min(len(self._board) - self._x, len(self._board[0]) - self._y)  # For no out of range

        for i in range(1, max_right):
            if self._x + i < len(self._board) and self._y + i < len(self._board[0]) and self._board[self._x + i][self._y + i] == 1:
                self._right_diagonal_moves.append((self._x + i, self._y + i))

    def get_right_diagonal_moves(self):
        return self._right_diagonal_moves

    def set_left_diagonal_moves(self):
        self._left_diagonal_moves.clear()
        min_right = min(self._x + 1, len(self._board[0]) - self._y)  # For no out of range, top-right to bottom-left
        for i in range(1, min_right):
            if self._x - i >= 0 and self._y + i < len(self._board[0]) and self._board[self._x - i][self._y + i] == 1:
                self._left_diagonal_moves.append((self._x - i, self._y + i))

        max_left = min(len(self._board) - self._x, self._y + 1)  # For no out of range, bottom-left to top-right
        for i in range(1, max_left):
            if self._x + i < len(self._board) and self._y - i >= 0 and self._board[self._x + i][self._y - i] == 1:
                self._left_diagonal_moves.append((self._x + i, self._y - i))

    def get_left_diagonal_moves(self):
        return self._left_diagonal_moves

    def get_possible_moves(self, x, y):
        self._x = x
        self._y = y
        self.set_vertical_moves()
        self.set_horizontal_moves()
        self.set_right_diagonal_moves()
        self.set_left_diagonal_moves()
        return self.get_vertical_moves(), self.get_horizontal_moves(), self.get_right_diagonal_moves(), self.get_left_diagonal_moves()
