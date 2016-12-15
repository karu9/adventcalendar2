from copy import copy
import sys
sys.setrecursionlimit(15000000)
#last one is the position of the elevator#
#even are chips, odds are generators
position = [[0,0],[1,0],[1,0],[2,2],[2,2],[0,0]]
elevatorMap = {0: [1], 1:[2, 0], 2:[3, 1], 3:[2]}
solutions = []
visited = []
visited.append(position)
def possible(pos):
    if pos[-1][1] == 25:
        return False
    else:
        for visit in visited:
            if pos[-1][0] == visit[-1][0] and pos[:-1] == visit[:-1]:
                if pos[-1][1] < visit[-1][1]:
                    return True
                else:
                    return False
        for i in range(5):
            if pos[i][0] != pos[i][1]:
                for j in range(5):
                    if pos[i][0] == pos[j][1]:
                        return False
        visited.append(pos)
        return True
def move(poss):
    if poss[:-1] == [[3,3]*5]:
        solutions.append(poss[-1])
        return
    startPos = poss[-1]
    for pos in elevatorMap[startPos[0]]:
        thingsInFloor = []
        for x in range(5):
            for y in range(2):
                if poss[x][y] == startPos[0]:
                    thingsInFloor.append((x,y))
        for i in range(len(thingsInFloor)):
            for j in range(i, len(thingsInFloor)):
                currposs = copy(poss)
                currposs[thingsInFloor[i][0]] = copy(poss[thingsInFloor[i][0]])
                currposs[thingsInFloor[i][0]][thingsInFloor[i][1]] = pos
                currposs[thingsInFloor[j][0]] = copy(poss[thingsInFloor[j][0]])
                currposs[thingsInFloor[j][0]][thingsInFloor[j][1]] = pos
                currposs[-1] = [pos, startPos[1]+1]
                if possible(sorted(currposs[:-1])+[currposs[-1]]):
                    move(currposs)
move(position)
print(solutions)
