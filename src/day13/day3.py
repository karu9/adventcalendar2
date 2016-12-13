import sys
sys.setrecursionlimit(15000000)
#createthemaze#
maxX = 60
maxY = 70
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
solutionsWithin50Steps = []
def onTheMaze(i, j, steps, dontReVisit):
    #ignore if position is negative or higher then limits#
    if i < 0 or j < 0 or i >= maxX or j >= maxY:
        return
    #ignore if position is a wall#
    if maze[i][j] == '♥':
        return
    #ignore if alreadyVisited in less steps#
    if dontReVisit :
        for visitedPosition in visitedPositions:
            visitedPositionArr = visitedPosition.split('-')
            if visitedPositionArr[0] == str(i)+','+str(j) and int(visitedPositionArr[1]) <= steps:
                return
        #found a solution#
        if maze[i][j] == 'O':
            solutionsSteps.append(steps)
            return
    else:
        if steps == 50 :
            if not str(i)+','+str(j) in solutionsWithin50Steps:
                solutionsWithin50Steps.append(str(i)+','+str(j))
            return
    if dontReVisit :
        visitedPositions.append(str(i)+','+str(j)+'-'+str(steps))
    onTheMaze(i+1, j, steps+1, dontReVisit)
    onTheMaze(i-1, j, steps+1, dontReVisit)
    onTheMaze(i, j-1, steps+1, dontReVisit)
    onTheMaze(i, j+1, steps+1, dontReVisit)
onTheMaze(1,1,0, True)
print(min(solutionsSteps), solutionsSteps)
visitedPositions = []
onTheMaze(1,1,0, False)
print(len(solutionsWithin50Steps), solutionsWithin50Steps)
