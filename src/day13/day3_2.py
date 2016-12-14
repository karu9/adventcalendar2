import sys
sys.setrecursionlimit(15000000)
#createthemaze#
maxX = 50
maxY = 50
maze = [['' for i in range(maxY)] for i in range(maxY)]
for i in range(maxX):
    for j in range(maxY):
        if format(i*i + 3*i + 2*i*j + j + j*j + 1352, 'b').count('1') % 2 == 0:
            maze[i][j] = ' '
        else :
            maze[i][j] = '♥'
maze[1][1] = ' '
#do the mazic !#
solutionsSteps = []
visitedPositions = []
distinctPositions = []
def onTheMaze(i, j, steps):
    if steps == 51 or maze[i][j] == '♥' or i < 0 or j < 0 or i >= maxX or j >= maxY or (i, j, steps) in visitedPositions:
        return
    else:
        visitedPositions.append((i, j, steps))
        if not (i, j) in distinctPositions:
            distinctPositions.append((i,j))
        onTheMaze(i+1, j, steps+1)
        onTheMaze(i-1, j, steps+1)
        onTheMaze(i, j-1, steps+1)
        onTheMaze(i, j+1, steps+1)
onTheMaze(1,1,0)
print(len(distinctPositions), distinctPositions)
