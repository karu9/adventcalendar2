import sys
sys.setrecursionlimit(15000)
inp = open("../../res/day2/input.txt", "r").readlines()
keypad =(("1","2","3"),("4","5","6"),("7","8","9"))
moves = ["U", "D", "R", "L"]
vect = [1, 1]
def readfile(inp, i, j):
    if j == len(inp) :
        return None
    elif i < len(inp[j]):
        move(inp[j][i])
        readfile(inp, i+1, j)
    else:
        print(keypad[vect[1]][vect[0]], end='')
        readfile(inp, 0, j+1)
def move(mov):
    if mov in moves :
        index = moves.index(mov)
        if index == 0 and vect[1] > 0 :
            vect[1] = vect[1] - 1
        elif index == 1 and vect[1] < 2 :
            vect[1] = vect [1] + 1
        elif index == 2 and vect[0] < 2 :
            vect[0] = vect [0] + 1
        elif index == 3 and vect[0] > 0 :
            vect[0] = vect[0] - 1
readfile(inp, 0, 0)
