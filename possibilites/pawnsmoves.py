class PawnRotate:
    def __init__(self, board):
        self._board = board

    def vertical_rotate(self, departure_x, departure_y, arrival_y):
        # Assurez-vous que departure_y est inférieur ou égal à arrival_y
        if departure_y > arrival_y:
            departure_y, arrival_y = arrival_y, departure_y

        # Parcourez la colonne à partir de departure_y + 1 jusqu'à arrival_y
        for i in range(departure_y + 1, arrival_y):
            if self._board[i][departure_x] == 4:
                self._board[i][departure_x] = 5
            elif self._board[i][departure_x] == 5:
                self._board[i][departure_x] = 4

        return self._board

    def right_diagonal_rotate(self, departure_x, departure_y):
        min_left = min(departure_x + 1, departure_y + 1)  # For no out of range
        for i in range(1, min_left):
            x, y = departure_x - i, departure_y - i
            if x != departure_x or y != departure_y:
                if self._board[x][y] == 4:
                    self._board[x][y] = 5
                elif self._board[x][y] == 5:
                    self._board[x][y] = 4

        max_right = min(len(self._board) - departure_x, len(self._board[0]) - departure_y)  # For no out of range
        for i in range(1, max_right):
            x, y = departure_x + i, departure_y + i
            if x != departure_x or y != departure_y:
                if self._board[x][y] == 4:
                    self._board[x][y] = 5
                elif self._board[x][y] == 5:
                    self._board[x][y] = 4
        return self._board

    def left_diagonal_rotate(self, departure_x, departure_y):
        # For no out of range, top-right to bottom-left
        min_right = min(departure_x + 1, len(self._board[0]) - departure_y)
        for i in range(1, min_right):
            x, y = departure_x - i + 1, departure_y + i - 1
            if x != departure_x or y != departure_y:
                if self._board[x][y] == 4:
                    self._board[x][y] = 5
                elif self._board[x][y] == 5:
                    self._board[x][y] = 4

        # For no out of range, bottom-left to top-right
        max_left = min(len(self._board) - departure_x, departure_y + 1)
        for i in range(1, max_left):
            x, y = departure_x + i, departure_y - i
            if x != departure_x or y != departure_y:
                if self._board[x][y] == 4:
                    self._board[x][y] = 5
                elif self._board[x][y] == 5:
                    self._board[x][y] = 4

        return self._board


