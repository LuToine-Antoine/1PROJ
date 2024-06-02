class PawnRotate:
    def __init__(self, board):
        self._board = board

    def vertical_rotate(self, departure_x, departure_y, arrival_y):
        # Ensure departure_y is less than or equal to arrival_y
        if departure_y > arrival_y:
            departure_y, arrival_y = arrival_y, departure_y

        # Traverse the column from departure_y + 1 to arrival_y
        for i in range(departure_y + 1, arrival_y):
            if self._board[i][departure_x] == 4:
                self._board[i][departure_x] = 5
            elif self._board[i][departure_x] == 5:
                self._board[i][departure_x] = 4

        return self._board

    def diagonal_rotate_up_left(self, departure_x, departure_y, arrival_x, arrival_y):
        for i in range(arrival_y + 1, departure_y):
            for j in range(arrival_x + 1, departure_x):
                if self._board[i][j] == 4:
                    self._board[i][j] = 5
                elif self._board[i][j] == 5:
                    self._board[i][j] = 4
            
    def diagonal_rotate_up_right(self, departure_x, departure_y, arrival_x, arrival_y):
        for i in range(arrival_y + 1, departure_y):
            for j in range(departure_x + 1, arrival_x):
                if self._board[i][j] == 4:
                    self._board[i][j] = 5
                elif self._board[i][j] == 5:
                    self._board[i][j] = 4
            
    def diagonal_rotate_down_left(self, departure_x, departure_y, arrival_x, arrival_y):
        for i in range(departure_y + 1, arrival_y):
            for j in range(arrival_x + 1, departure_x):
                if self._board[i][j] == 4:
                    self._board[i][j] = 5
                elif self._board[i][j] == 5:
                    self._board[i][j] = 4
            
    def diagonal_rotate_down_right(self, departure_x, departure_y, arrival_x, arrival_y):
        for i in range(departure_y + 1, arrival_y):
            for j in range(departure_x + 1, arrival_x):
                if self._board[i][j] == 4:
                    self._board[i][j] = 5
                elif self._board[i][j] == 5:
                    self._board[i][j] = 4
            


"""     def diagonal_rotate_left(self, departure_x, departure_y):
        # Top-left to bottom-right
        min_top_left = min(departure_x, departure_y)
        for i in range(1, min_top_left + 1):
            x, y = departure_x - i, departure_y - i
            if self._board[x][y] == 4:
                self._board[x][y] = 5
            elif self._board[x][y] == 5:
                self._board[x][y] = 4
        
    def diagonal_rotate_up_left(self, departure_x, departure_y, arrival_x, arrival_y):
        if departure_y > arrival_y:
            departure_y, arrival_y = arrival_y, departure_y
        if departure_x > arrival_x:
            departure_x, arrival_x = arrival_x, departure_x

        for i in range(departure_y + 1, arrival_y):
            for j in range(departure_x, arrival_x):
                if self._board[i][j] == 4:
                    self._board[i][j] = 5
                elif self._board[i][j] == 5:
                    self._board[i][j] = 4

        max_bottom_right = min(len(self._board) - departure_x, len(self._board[0]) - departure_y)
        for i in range(1, max_bottom_right):
            x, y = departure_x + i, departure_y + i
            if self._board[x][y] == 4:
                self._board[x][y] = 5
            elif self._board[x][y] == 5:
                self._board[x][y] = 4

        return self._board

    def diagonal_rotate_right(self, departure_x, departure_y):
        # Top-right to bottom-left
        min_top_right = min(departure_x, len(self._board[0]) - departure_y - 1)
        for i in range(1, min_top_right + 1):
            x, y = departure_x - i, departure_y + i
            if self._board[x][y] == 4:
                self._board[x][y] = 5
            elif self._board[x][y] == 5:
                self._board[x][y] = 4

        max_bottom_left = min(len(self._board) - departure_x, departure_y + 1)
        for i in range(1, max_bottom_left):
            x, y = departure_x + i, departure_y - i
            if self._board[x][y] == 4:
                self._board[x][y] = 5
            elif self._board[x][y] == 5:
                self._board[x][y] = 4

        return self._board
 """