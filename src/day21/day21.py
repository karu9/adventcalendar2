from copy import copy
from random import shuffle
lines = open("input.txt", 'r').readlines()
def swap(i, j, inp):
    tempinp = copy(inp)
    if i != 0 and j!= len(inp)-1:
        tempinp = tempinp[:i] + inp[j] + tempinp[i+1:]
        tempinp = tempinp[:j] + inp[i] + tempinp[j+1:]
    else:
        if i == 0:
            if j!= len(inp)-1:
                tempinp = inp[j] + tempinp[1:]
                tempinp = tempinp[:j] + inp[i] + tempinp[j+1:]
            else :
                tempinp = inp[j] + tempinp[1:]
                tempinp = tempinp[:-1] + inp[i]
        else :
            tempinp = tempinp[:i] + inp[j] + tempinp[i+1:]
            tempinp = tempinp[:-1] + inp[i]
    return tempinp
def rotate(toRight, steps, inp):
    for i in range(steps):
        if toRight :
            inp = inp[-1]+inp[:-1]
        else:
            inp = inp[1:]+inp[0]
    return inp
def reverse(i, j, inp):
    tempinp = copy(inp)
    if j != len(inp) - 1 :
        tempinp = inp[:i] + ''.join(reversed(inp[i:j+1])) + inp[j+1:]
    else :
        tempinp = inp[:i] + ''.join(reversed(inp[i:]))
    return tempinp
def move(i, j, inp):
    tempinp = copy(inp)
    tempinp = tempinp[:i] + tempinp[i+1:]
    tempinp = tempinp[:j] + inp[i] + tempinp[j:]
    return tempinp
def encrypt(inp):
    for line in lines:
        splitLine = line[:-1].split(' ')
        if line.startswith("swap position"):
            inp = swap(int(splitLine[2]), int(splitLine[5]), inp)
        elif line.startswith("swap letter"):
            inp = swap(inp.index(splitLine[2]), inp.index(splitLine[5]), inp)
        elif line.startswith("rotate left"):
            inp = rotate(False, int(splitLine[2]), inp)
        elif line.startswith("rotate right"):
            inp = rotate(True, int(splitLine[2]), inp)
        elif line.startswith("rotate based"):
            rot = inp.index(splitLine[6])
            if rot > 3:
                rot +=1
            rot += 1
            inp = rotate(True, rot, inp)
        elif line.startswith("reverse positions"):
            inp = reverse(int(splitLine[2]), int(splitLine[4]), inp)
        elif line.startswith("move position"):
            inp = move(int(splitLine[2]), int(splitLine[5]), inp)
        else:
            print('errorrrr')
    return inp
#part 1#
print(encrypt("abcdefgh"))
#part 2#
shuffledList = list("abcdefgh")
shuffle(shuffledList)
shuffled = ''.join(shuffledList)
while encrypt(shuffled) != "fbgdceah":
    shuffledList = list("abcdefgh")
    shuffle(shuffledList)
    shuffled = ''.join(shuffledList)
print(shuffled)
