plateau = [
    [0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0],
    [0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0],
    [0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1],
    [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0],
    [0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0],
    [0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0]
]

def see_board():
    for i in range(11):
        for j in range(19):
            if plateau[i][j] == 0:
                print(" ", end='')
            else:
                print("o", end='')
        print(" ")