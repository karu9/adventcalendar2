lines = open('input.txt','r').readlines()
nodes = []
#nodes as created such as :
#0 is x, 1 is y, 2 is size, 3 is used, 4 is avail, 5 is percent filled
def getAdjacents(node, nodes):
    adjacents = []
    for nod in nodes:
        if abs(nod[0]-node[0]) + abs(nod[1]-node[1]) == 1:
            adjacents.append(nod)
    return adjacents
def getAdjViablePairs(node, nodes):
    adjacents = getAdjacents(node, nodes)
    viable = []
    for adj in adjacents :
        if node[3] != 0 and adj[4] >= node[3]:
            viable.append((node, adj))
    print(viable)
    return viable
def getViablePairs(node, nodes):
    viable = []
    for nod in nodes :
        if nod != node and node[3] != 0 and nod[4] >= node[3]:
            viable.append((node, nod))
    return viable
for line in lines :
    rawNode = line.strip().split()
    node = [int(rawNode[0].split('-')[1][1:]), int(rawNode[0].split('-')[2][1:]), int(rawNode[1][:-1]), int(rawNode[2][:-1]), int(rawNode[3][:-1]), int(rawNode[4][:-1])]
    nodes.append(node)
viables = []
for node in nodes :
    vias = getViablePairs(node, nodes)
    if len(vias) != 0:
        for pair in vias:
            viables.append(pair)
#part 1#
print(len(viables))
#part 2#
goalData = [max(list(map(lambda x : x[0], nodes))), 0]
goalSpot = (0,0)
