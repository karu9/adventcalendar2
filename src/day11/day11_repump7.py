from copy import copy
import itertools
import sys
sys.setrecursionlimit(15000000)
possibleStates = []
impossibleStatesForState = {}
possibleFloors = {1: [1], 2:[1, -1], 3:[1, -1], 4:[-1]}
visited = {}
impossibles = []
solutions = []
for i in range(1, 5):
    for j in range(1, 5):
        possibleStates.append(10*i+j)
for state in possibleStates:
    impossibleStatesForState[state] = []
    if not state in [11,22,33,44]:
        chip = str(state)[0]
        for i in range(1, 5):
           impossibleStatesForState[state].append(i*10 + int(chip)) 
def possible(state, count):
    if state in impossibles:
        return False
    elif state in visited.keys():
        if visited[state] < count:
            return False
        else :
            visited[state] = count
            return True
    stateString = str(state)
    listStates = [int(stateString[x] + stateString[x+1]) for x in range(0, 10, 2)]
    for i in range(5):
        for j in range(5):
            if i != j and listStates[j] in impossibleStatesForState[listStates[i]]:
                impossibles.append(state)
                return False
    visited[state] = count
    return True
def move(start, count):
    if start == 44444444444:
        solutions.append(start)
        print(start)
    else:
        floor = int(str(start)[10])
        startString = str(start)
        for possibleFloor in possibleFloors[floor]:
            posThingsInFloor = [i for i in list(filter(lambda x : int(startString[x]) == floor, range(10)))]
            for i in range(len(posThingsInFloor)):
                for j in range(i, len(posThingsInFloor)):
                    nextStart = start
                    nextStart += possibleFloor * 10 ** (len(startString) - posThingsInFloor[i]-1)
                    if i != j:  
                        nextStart += possibleFloor * 10 ** (len(startString) - posThingsInFloor[j]-1)
                    nextStartString = str(nextStart)
                    nextStart = int(''.join(sorted([nextStartString[x] + nextStartString[x+1] for x in range(0, 10, 2)]) + [str(floor + possibleFloor)]))
                    if count != 50 and possible(nextStart, count+1):
                        move(nextStart, count+1)
move(11111111111, 0)
print(solutions)
    
