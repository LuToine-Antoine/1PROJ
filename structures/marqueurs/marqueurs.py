import plateau

for i in range(11):
    for j in range(19):
        if plateau.plateau[i][j] == 0:
            print(" ", end='')
        else:
            print("o", end='')
    print(" ")
