import sys
sys.setrecursionlimit(15000000)
from hashlib import md5
inp = 'pxxbnzuo'
opened = 'bcdef'
mapping = {0:'U', 1:'D', 2:'L', 3:'R'}
mappingXY = {0:(0,1), 1:(0,-1), 2:(-1,0), 3:(1,0)}
solutions = []
def getHash(string):
    hashh = md5()
    hashh.update(string.encode('utf-8'))
    return hashh.hexdigest()[:4]
def move(path, x, y):
    if x == 3 and y == 0:
        solutions.append(path)
    else:
        hashes = getHash(inp + path)
        for i in range(4):
            if hashes[i] in opened:
                newX = x + mappingXY[i][0]
                newY = y + mappingXY[i][1]
                if newX <= 3 and newX >= 0 and newY <= 3 and newY >= 0:
                    move(path + mapping[i], newX, newY)
move('', 0, 3)
print(min(solutions))
print(max([len(i) for i in solutions]))
