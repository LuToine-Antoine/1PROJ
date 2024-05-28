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
                break
            elif self._board[self._x][i] == 2 or self._board[self._x][i] == 3:
                continue
            elif self._board[self._x][i] == 1:
                self._horizontal_moves.append((self._x, i))
                break

        for j in range(self._y - 1, -1, -1):
            if self._board[self._x][j] == 4 or self._board[self._x][j] == 5:
                break
            elif self._board[self._x][j] == 2 or self._board[self._x][j] == 3:
                continue
            elif self._board[self._x][j] == 1:
                self._horizontal_moves.append((self._x, j))
                break

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
