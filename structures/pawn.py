class Paws:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board
        self._stock = False
        self._pawn_stock = 1

    def empty_stock(self, board):
        """
        Check if stock is empty or not
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 4 or board[i][j] == 5:
                    self._pawn_stock -= 1

        self._stock = self._pawn_stock
        if self._pawn_stock <= 0:
            self._pawn_stock = True # Stock is empty

    def get_stock(self):
        """
        Get the stock to check if it's empty or not
        """
        return self._stock

    def get_pawn_stock(self):
        """
        Get the number of pawns in the stock
        """
        return self._pawn_stock

    def put_paws(self, x, y, board, player):
        """
        Use for player to put their paws on the board.
        """
        self._x = x
        self._y = y

        if player == 1:
            self._board[self._x][self._y] = 4  # Change the state of the case of the board Player 1
        elif player == 2:
            self._board[self._x][self._y] = 5  # Change the state of the case of the board Player 2
        return board



