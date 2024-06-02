class PawnRotate:
    def __init__(self, board):
        self._board = board

    def vertical_rotate(self, departure_x, departure_y, arrival_y):
        # Check if the departure_y is greater than the arrival_y
        if departure_y > arrival_y:
            departure_y, arrival_y = arrival_y, departure_y

        for i in range(departure_y + 1, arrival_y):
            if self._board[i][departure_x] == 4:
                self._board[i][departure_x] = 5
            elif self._board[i][departure_x] == 5:
                self._board[i][departure_x] = 4

        return self._board

    #for all diagonal directions, taking directions into account, do the rotate function

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
            
