lines = open('input.txt', 'r').readlines()
discs = list(map(lambda x: (int(lines[x][:-2].split(' ')[3]), int(lines[x][:-2].split(' ')[11])), range(len(lines))))
def getCapsule():
    index = 0
    while True:
        if len(list(filter(lambda x: (discs[x][1]+x+index) % discs[x][0] != 0, range(len(discs))))) == 0:
            return(index-1)
        index += 1
print(getCapsule())  #part1# 
discs.append((11, 0))
print(getCapsule()) #part2#
