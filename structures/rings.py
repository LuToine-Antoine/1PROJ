class Rings:
    def __init__(self, x, y, board):
        self._x = x
        self._y = y
        self._board = board

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

