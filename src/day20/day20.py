lines = open("input.txt", 'r').readlines()
linesNumber = sorted(list(map(lambda x : (int(x.split('-')[0]), int(x.split('-')[1][:-1])), lines)))
def getOverlapping(lis):
    ret = []
    for line in lis:
        reduced = False
        for line2 in lis:
            if line2[0]<line[1] and line2[1]> line[1]:
                if not (line[0], line2[1]) in ret:
                    ret.append((line[0], line2[1]))
                    reduced = True
            elif line2[0]<line[0] and line2[1]> line[0]:
                if not (line2[0], line[1]) in ret:
                    ret.append((line2[0], line[1]))
                    reduced = True
        if not reduced:
            ret.append(line)
    return sorted(ret)
#remove redundant#
redundant = []
for line in linesNumber:
    for line2 in linesNumber:
        if line2[0]> line[0] and line2[1]<line[1]:
            if not line2 in redundant:
                redundant.append(line2)
for line in redundant :
    linesNumber.remove(line)
#merge overlapping#
newList = getOverlapping(linesNumber)
while len(newList) != len(linesNumber):
    linesNumber = newList
    newList = getOverlapping(linesNumber)
linesNumber = newList
#take the first occurence where max of previsous is different from min of next
for i in range(len(newList)-1):
    if newList[i][1] != newList[i+1][0]:
        print(newList[i], newList[i+1])
        break

