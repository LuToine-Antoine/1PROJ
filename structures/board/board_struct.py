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
        for i in range(11):
            for j in range(19):
                if self.board[i][j] == 0:  # Case impossible
                    print(" ", end='')
                elif self.board[i][j] == 1: # Case vide
                    print("o", end='')
                elif self.board[i][j] == 2:  # Anneau du joueur 1
                    print("1", end='')
                elif self.board[i][j] == 3:  # Anneau du joueur 2
                    print("2", end='')
                elif self.board[i][j] == 4:  # Pion du joueur 1
                    print("3", end='')
                else: # Pion du joueur 2
                    print("4", end='')
            print(" ")

    def put_rings(self, board):
        '''
        Use only in start of game, to put rings on the board.
        '''
        ring_round = 0

        while ring_round < 2 :
            print("Pion en placement : ", ring_round + 1)
            xring_player_1 = int(input("Player 1, (x) where do you want to put your ring? : "))
            yring_player_1 = int(input("Player 1, (y) where do you want to put your ring? : "))

            # Ces boucles vériient si les coordonnées sont valides (comprise dans le plateau mais aussi case vide)
            while self.board[0][0] <= xring_player_1 > len(self.board) or self.board[0][0] <= yring_player_1 > len(self.board) or self.board[xring_player_1][yring_player_1] != 1 :
                xring_player_1 = int(input("Player 1, invalid x ring : "))
                yring_player_1 = int(input("Player 1, invalid y ring : "))
            self.board[xring_player_1][yring_player_1] = 2  # Changer l'état de la case du plateau

            xring_player_2 = int(input("Player 2, (x) where do you want to put your ring? : "))
            yring_player_2 = int(input("Player 2, (y) where do you want to put your ring? : "))

            while self.board[0][0] <= xring_player_2 > len(self.board) or self.board[0][0] <= yring_player_2 > len(self.board) or self.board[xring_player_2][yring_player_2] != 1 :
                xring_player_2 = int(input("Player 2, invalid x ring? : "))
                yring_player_2 = int(input("Player 2, invalid y ring? : "))
            self.board[xring_player_2][yring_player_2] = 3  # Changer l'état de la case du plateau
            ring_round += 1

        return board


board = BoardStruct()
board.put_rings(board)
board.see_board()