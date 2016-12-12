import sys
sys.setrecursionlimit(15000000)
import copy
#0=microchip, 1=generator#
#0=thulim, 1=plutonium, 2=strontium, 3=promethium, 4=ruthenium#
objects = [(1,0),(0,0),(1,1),(1,2),(0,1),(0,2),(1,3),(0,3),(1,4),(0,4)]
#last one is the position of the elevator#
positions = [0,0,0,0,1,1,2,2,2,2,0]
alreadyVisited = [positions + [0]]
solutions = []
def arePossible(poss, count):
    for visited in alreadyVisited:
        if poss == visited[:-1]:
            if count >= visited[len(visited)-1]:
                return False
            else:
                alreadyVisited.remove(visited)
                break
    for i in range(len(poss)-1):
        if not isPossible(i, poss):
            return False
    return True
def isPossible(ind, poss):
    #if it's a generator, no issue#
    if objects[ind][0] == 1:
        return True
    #else#
    ret = True
    for i in range(len(poss)-1):
        if i != ind:
            if positions[ind] == positions[i]:
                if objects[ind][1] == objects[i][1] and objects[i][0] == 1:
                    return True
                elif objects[ind][1] != objects[i][1] and objects[i][0] == 1:
                    ret = False
    return ret
def move(poss, count):
    if poss in [[3]*11]:
        solutions.append(count)
    else:
        elevatorPos = poss[10]
        coordsObjAtPos = [i for i, x in enumerate(poss[:-1]) if x == elevatorPos]
        possiblePoss = []
        if elevatorPos == 0:
            possiblePoss.append(1)
        elif elevatorPos == 3:
            possiblePoss.append(2)
        else :
            possiblePoss = [elevatorPos-1, elevatorPos+1]
        for possiblePos in possiblePoss:
            #move one obj#
            for coord in coordsObjAtPos:
                newPoss = copy.copy(poss)
                newPoss[coord] = possiblePos
                newPoss[10] = possiblePos
                if arePossible(newPoss, count):
                    alreadyVisited.append(newPoss+[count])
                    move(newPoss, count+1)
            #move two obj#
            if len(coordsObjAtPos) >= 2:
                for i in range(len(coordsObjAtPos)-1):
                    for j in range(i, len(coordsObjAtPos)):
                        newPoss = copy.copy(poss)
                        newPoss[coordsObjAtPos[i]] = possiblePos
                        newPoss[coordsObjAtPos[j]] = possiblePos
                        newPoss[10] = possiblePos
                        if arePossible(newPoss, count):
                            alreadyVisited.append(newPoss+[count])
                            move(newPoss, count+1)
move(positions, 0)
print(min(solutions))

