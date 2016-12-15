from copy import copy
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
        possibleStates.append(str(i)+str(j))
        for state in possibleStates:
            if not state in impossibleStatesForState.keys():
                impossibleStatesForState[state] = []
            if state[0] == str(j) and not state[0] == state[1]:
                impossibleStatesForState[state].append(str(i)+str(j))
def possible(state, count):
    stateString = str(state)[:11]
    if count == 42 or int(stateString[:-1]) in impossibles:
        return False
    elif int(stateString) in visited.keys():
        if visited[int(stateString)] < count:
            return False
        else :
            visited[int(stateString)] = count
            return True
    listStates = [stateString[x] + stateString[x+1] for x in range(0, 10, 2)]
    for i in range(5):
        for j in range(i, 5):
            if listStates[j] in impossibleStatesForState[listStates[i]]:
                impossibles.append(int(stateString[:-1]))
                return False
    visited[int(stateString)] = count
    return True
def move(start, count):
    floor = int(str(start)[10])
    startString = str(start)
    if floor == 4 and str(start)[:10] == '4' * 10:
        solutions.append(start)
    else:
        stateString = str(start)[:10]
        for possibleFloor in possibleFloors[floor]:
            posThingsInFloor = [i for i in list(filter(lambda x : int(startString[x]) == floor, range(10)))]
            for i in range(len(posThingsInFloor)):
                for j in range(i, len(posThingsInFloor)):
                    nextStart = start
                    nextStart += possibleFloor * 10 ** (len(startString) - posThingsInFloor[i])
                    if i != j:  
                        nextStart += possibleFloor * 10 ** (len(startString) - posThingsInFloor[j])
                    nextStart += possibleFloor * 10
                    if possible(nextStart, count):
                        move(nextStart, count)
move(33332121111, 0)
print(solutions)
    
