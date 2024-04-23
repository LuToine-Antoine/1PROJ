class BoardStruct:

    def __init__(self):
        self.board = [
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
        ]

    def see_board(self):
        """
        Displays the board and the players rings and pawns in the terminal.
        :return: nothing
        """

        for i in range(11):
            for j in range(19):
                if self.board[i][j] == 0:  # Invalid case
                    print(" ", end='')
                elif self.board[i][j] == 1:  # Empty case
                    print("o", end='')
                elif self.board[i][j] == 2:  # Player 1 rings
                    print("1", end='')
                elif self.board[i][j] == 3:  # Player 2 rings
                    print("2", end='')
                elif self.board[i][j] == 4:  # Player 1 pawns
                    print("3", end='')
                else:  # Player 2 pawns
                    print("4", end='')
            print(" ")


board = BoardStruct()
board.see_board()
