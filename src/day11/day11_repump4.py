import sys
from random import shuffle
sys.setrecursionlimit(15000000)
#last one is the position of the elevator#
#even are chips, odds are generators
positions = [0,0,1,0,1,0,2,2,2,2,0]
elevatorMap = {0: [1], 1:[2, 0], 2:[3, 1], 3:[2]}
solutions = []
def isPossible(count):
    if count == 15:
        return False
    for chip in range(0, 10, 2):
        if positions[chip] != positions[chip+1]:
            if len(list(filter(lambda x : positions[x] == positions[chip], range(1, 11, 2)))) != 0:
                return False
    return True
def move(count):
    if positions == [3]*11:
        print(count)
    floor = positions[10]
    thingsOnThisFloor = list(filter(lambda x : positions[x] == floor, range(10)))
    for i in range(len(thingsOnThisFloor)):
        for j in range(i, len(thingsOnThisFloor)):
            for possibleFloor in elevatorMap[floor]:
                positions[thingsOnThisFloor[i]] = possibleFloor
                positions[thingsOnThisFloor[j]] = possibleFloor
                positions[10] = possibleFloor
                if isPossible(count):
                    move(count+1)
                positions[thingsOnThisFloor[i]] = floor
                positions[thingsOnThisFloor[j]] = floor
                positions[10] = floor
move(0)
