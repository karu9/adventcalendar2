import sys
from random import shuffle
sys.setrecursionlimit(15000000)
#last one is the position of the elevator#
positions = [0,0,1,0,1,0,2,2,2,2,0]
visitedSolutions = []
solutions = []
def isPossible(count):
    if count > 200:
        return False
    for visited in visitedSolutions:
        if ''.join(visited.split(',')[:-1]) == ''.join(map(str,positions)):
            if int(visited.split(',')[-1]) <= count:
                return False
            else:
                visitedSolutions.remove(visited)
                return True
    for i in range(0, 5, 2):
        coordsObjAtPos = list(filter(lambda x : positions[x] == positions[i], range(10)))
        if not i+1 in coordsObjAtPos:
            if len(list(filter(lambda x : x % 2 == 1, coordsObjAtPos))) != 0:
                return False
    return True            
def move(count):
    if  positions == [3]*11:
        solutions.append(count)
        print(solutions)
    else:
        elevatorPos = positions[10]
        coordsObjAtPos = list(filter(lambda x : positions[x] == elevatorPos, range(10)))
        possiblePoss = []
        if elevatorPos == 0:
            possiblePoss.append(1)
        elif elevatorPos == 3:
            possiblePoss.append(2)
        else :
            possiblePoss = [elevatorPos-1, elevatorPos+1]
            shuffle(possiblePoss)
        for possiblePos in possiblePoss:
            #move one obj#
            for coord in coordsObjAtPos:
                positions[coord] = possiblePos
                positions[10] = possiblePos
                count += 1
                if isPossible(count):
                    visitedSolutions.append(','.join(map(str, positions))+','+str(count))
                    move(count)
                count -= 1
                positions[coord] = elevatorPos
                positions[10] = elevatorPos
            #move two obj#
            if len(coordsObjAtPos) >= 2:
                for i in range(len(coordsObjAtPos)-1):
                    for j in range(i, len(coordsObjAtPos)):
                        positions[coordsObjAtPos[i]] = possiblePos
                        positions[coordsObjAtPos[j]] = possiblePos
                        positions[10] = possiblePos
                        count += 1
                        if isPossible(count):
                            visitedSolutions.append(','.join(map(str, positions))+','+str(count))
                            move(count)
                        count -= 1
                        positions[coordsObjAtPos[i]] = elevatorPos
                        positions[coordsObjAtPos[j]] = elevatorPos
move(0)
print(min(solutions))

