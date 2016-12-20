from copy import copy
possiblePos = []
possibleMoves = {1: [1], 2:[1, -1], 3:[1, -1], 4:[-1]}
visited = {}
for i in range(1,5):
    for j in range(1,5):
        possiblePos.append(10*i + j)
impossiblePosForPos = {}
possibleNextPosForPos = {}
results = []
for pos in possiblePos:
    for lvl in range(1, 5):
        for lvl2 in range(1, 5):
                if(abs(lvl2-lvl) == 1):
                    possibleNextPosForPos[(pos, lvl, lvl2)] = []
                    for i in range(2):
                        if str(lvl) == str(pos)[i]:
                            nextPos = lvl2 * (10 ** ((i+1)%2)) + int(str(pos)[(i+1)%2]) * (10**i)
                            possibleNextPosForPos[(pos, lvl, lvl2)].append(nextPos)
for pos in possiblePos:
    impossiblePosForPos[pos] = []
    if not pos in [11,22,33,44]:
        chip = str(pos)[0]
        for i in range(1, 5):
           impossiblePosForPos[pos].append(i*10 + int(chip))
class Position :
    def __init__(self, pos, lvl, cnt):
        self.pos = pos
        self.lvl = lvl
        self.cnt = cnt
        self.previousPos = None
    def setPrevious(self,pos):
        self.previousPos = pos
    def moveToNext(self):
        for nextPos in self.nextPos():
            if nextPos.pos == [44]*7:
                results.append(nextPos)
            else:
                nextPos.moveToNext()
    def nextPos(self):
        nextPositions = []
        for possibleMove in possibleMoves[self.lvl]:
            for i in range(7):
                for j in range(7):
                    if i != j:
                        for nextPos in possibleNextPosForPos[(self.pos[i], self.lvl,self.lvl + possibleMove)]: 
                            for nextPos2 in possibleNextPosForPos[(self.pos[j], self.lvl, self.lvl + possibleMove)]:
                                pos = copy(self.pos)
                                pos[i] = nextPos
                                pos[j] = nextPos2
                                nextPosition = Position(sorted(pos), self.lvl + possibleMove, self.cnt + 1)
                                if nextPosition.possible():
                                    nextPosition.setPrevious(self)
                                    nextPositions.append(nextPosition)
                for nextPos in possibleNextPosForPos[(self.pos[i], self.lvl, self.lvl + possibleMove)]:
                    pos = copy(self.pos)
                    pos[i] = nextPos
                    nextPosition = Position(sorted(pos), self.lvl + possibleMove, self.cnt + 1)
                    if nextPosition.possible():
                        nextPosition.setPrevious(self)
                        nextPositions.append(nextPosition)
        return nextPositions  
    def possible(self):
        state = str(self.pos + [self.lvl])
        if state in visited.keys():
            if self.cnt >= visited[state]:
                return False
        visited[state] = self.cnt
        for i in range(7):
            for j in range(7):
                if i != j and self.pos[j] in impossiblePosForPos[self.pos[i]]:
                    return False
        mandatorySteps = sum(list(map(lambda x : 8 - (int(str(x)[0]) + int(str(x)[1])), self.pos)))
        if self.cnt + mandatorySteps > 100:
            return False
        return True
position = Position([11, 11, 11, 21, 21, 33, 33], 1, 0)
position.moveToNext()
print(min(list(map(lambda x: x.cnt, results))))
