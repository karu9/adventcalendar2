lines = open("input.txt", 'r').readlines()
linesNumber = sorted(list(map(lambda x : (int(x.split('-')[0]), int(x.split('-')[1][:-1])), lines)))
def getOverlapping(lis):
    ret = []
    for line in lis:
        reduced = False
        for line2 in lis:
            if line != line2:
                if line2[0]<=line[1] and line2[1]>= line[1]:
                    reduced = True
                    if not (line[0], line2[1]) in ret:
                        ret.append((line[0], line2[1]))
                elif line2[0]<=line[0] and line2[1]>= line[0]:
                    reduced = True
                    if not (line2[0], line[1]) in ret:
                        ret.append((line2[0], line[1]))
        if not reduced:
            ret.append(line)
    return sorted(ret)
def removeRedundant(lis):
    redundant = []
    for line in lis:
        for line2 in lis:
            if line != line2:
                if line2[0]>= line[0] and line2[1]<= line[1]:
                    if not line2 in redundant:
                        redundant.append(line2)
    for line in redundant :
        lis.remove(line)
#remove redundant#

#merge overlapping#
removeRedundant(linesNumber)
newList = getOverlapping(linesNumber)
while len(newList) != len(linesNumber):
    linesNumber = newList
    newList = getOverlapping(linesNumber)
    removeRedundant(newList)
#take the first occurence where max of previsous is different from min of next
for i in range(len(newList)-1):
    if newList[i][1] != newList[i+1][0] and newList[i][1] + 1 != newList[i+1][0]:
        print(newList[i], newList[i+1])
        break
#part 2: count:
count = 4294967296
for line in newList:
    count -= line[1] - (line[0] - 1)
print(count)

