import sys
sys.setrecursionlimit(15000000)
#0=microchip, 1=generator#
#0=thulim, 1=plutonium, 2=strontium, 3=promethium, 4=ruthenium#
objects = [(1,0),(0,0),(1,1),(1,2),(0,1),(0,2),(1,3),(0,3),(1,4),(0,4)]
#last one is the position of the elevator#
positions = [0,0,0,0,1,1,2,2,2,2,0]
solutions = []
def arePossible(count):
    if count > 250:
        return False
    for i in range(10):
        if not isPossible(i):
            return False
    return True
def isPossible(ind):
    #if it's a generator, no issue#
    if objects[ind][0] == 1:
        return True
    #else#
    ret = True
    for i in range(10):
        if i != ind:
            if positions[ind] == positions[i]:
                if objects[ind][1] == objects[i][1]:
                    return True
                elif objects[ind][1] != objects[i][1] and objects[i][0] == 1:
                    ret = False
    return ret
def move(count):
    print(count, positions)
    if positions == [3]*11:
        solutions.append(count)
        print(solution)
    else:
        elevatorPos = positions[10]
        coordsObjAtPos = [i for i, x in enumerate(positions[:-1]) if x == elevatorPos]
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
                positions[coord] = possiblePos
                positions[10] = possiblePos
                count += 1
                if arePossible(count):
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
                        if arePossible(count):
                            move(count)
                        count -= 1
                        positions[coordsObjAtPos[i]] = elevatorPos
                        positions[coordsObjAtPos[j]] = elevatorPos
move(0)
print(min(solutions))

