import sys
sys.setrecursionlimit(15000000)
#createthemaze#
maxX = 50
maxY = 50
maze = [['' for i in range(maxY)] for i in range(maxY)]
def isEven(i, j):
    return format(i*i + 3*i + 2*i*j + j + j*j + 1352, 'b').count('1') % 2 == 0
for i in range(maxX):
    for j in range(maxY):
        if isEven(i,j):
            maze[i][j] = ' '
        else :
            maze[i][j] = '♥'
maze[1][1] = 'X'
maze[31][39] = 'O'
#do the mazic !#
visitedPositions = []
solutionsSteps = []
def onTheMaze(i, j, steps):
    #ignore if position is negative or higher then limits#
    if i < 0 or j < 0 or i >= maxX or j >= maxY:
        return
    #ignore if position is a wall#
    if maze[i][j] == '♥':
        return
    #ignore if alreadyVisited in less steps#
    for visitedPosition in visitedPositions:
        visitedPositionArr = visitedPosition.split('-')
        if visitedPositionArr[0] == str(i)+','+str(j) and int(visitedPositionArr[1]) <= steps:
            return
        #found a solution#
    if maze[i][j] == 'O':
        solutionsSteps.append(steps)
        return
    visitedPositions.append(str(i)+','+str(j)+'-'+str(steps))
    onTheMaze(i+1, j, steps+1)
    onTheMaze(i-1, j, steps+1)
    onTheMaze(i, j-1, steps+1)
    onTheMaze(i, j+1, steps+1)
onTheMaze(1,1,0)
print(min(solutionsSteps), solutionsSteps)
visitedPositions = []
