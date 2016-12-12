import sys
sys.setrecursionlimit(15000000)
class Thing :
    def __init__(self, typ, element, floor):
        self.typ  =  typ
        self.element = element
        self.floor = floor
    def isGenerator(self):
        return self.typ == 'g'
    def sameElement(self, thing):
        return thing.element == self.element
    def safe(self, things):
        ret = True
        if self.typ == 'm':
            for thing in things:
                if thing.isGenerator() and not self.sameElement(thing):
                    ret = False
                if thing.isGenerator() and self.sameElement(thing):
                    return True
        return ret
def getThingsOnFloor(things, floor):
    ret = []
    for thing in things:
        if thing.floor  == floor:
            ret.append(thing)
    return ret
def safe(things):
    for thing in things:
        if not thing.safe(getThingsOnFloor(things, thing.floor)):
            return False
    return True
def isAlreadyVisited(things, alreadyVisited, floor):
    listVisit = list(map(lambda x : x.floor, things))
    listVisit.append(floor)
    if listVisit in alreadyVisited :
        return True
    return False
def addVisited(things, alreadyVisted, floor):
    listVisit = list(map(lambda x : x.floor, things))
    listVisit.append(floor)
    alreadyVisited.append(listVisit)
def removeVisited(things, alreadyVisted, floor):
    listVisit = list(map(lambda x : x.floor, things))   
    listVisit.append(floor)
    alreadyVisited.remove(listVisit)
def move(floor, movecount, things, alreadyVisited):
    allinsamefloor = True
    for thing in things:
        if thing.floor != things[0].floor:
            allinsamefloor = False
            break
    if allinsamefloor:
        print(movecount, list(map(lambda x : x.floor, things)), floor)
    else :
        thingsonfloor = getThingsOnFloor(things, floor)
        possiblefloors = []
        if floor == 0:
            possiblefloors.append(1)
        elif floor == 3:
            possiblefloors.append(2)
        else:
            possiblefloors = [floor-1, floor+1]
        for possiblefloor in possiblefloors:
            #try to move one thing#
            for thing in thingsonfloor:
                thing.floor = possiblefloor
                isalreadyvisited = isAlreadyVisited(things, alreadyVisited, possiblefloor)
                if safe(things) and not isalreadyvisited:
                    addVisited(things, alreadyVisited, possiblefloor)
                    move(possiblefloor, movecount + 1, things, alreadyVisited) 
                    removeVisited(things, alreadyVisited, possiblefloor)
                thing.floor = floor
            #try to move two things#
            if len(thingsonfloor) >= 2:
                for i in range(len(thingsonfloor) - 1):
                    for j in range(i+1, len(thingsonfloor)):
                        thingsonfloor[i].floor = possiblefloor
                        thingsonfloor[j].floor = possiblefloor
                        isalreadyvisited = isAlreadyVisited(things, alreadyVisited, possiblefloor)
                        if safe(things) and not isalreadyvisited:
                            addVisited(things, alreadyVisited, possiblefloor)
                            move(possiblefloor, movecount + 1, things, alreadyVisited)
                            removeVisited(things, alreadyVisited, possiblefloor)
                        thingsonfloor[i].floor = floor
                        thingsonfloor[j].floor = floor
things = [Thing('g', 'th', 0),
          Thing('m', 'th', 0),
          Thing('g', 'pl', 0),
          Thing('g', 'st', 0),
          Thing('m', 'pl', 1),
          Thing('m', 'st', 1),
          Thing('g', 'pr', 2),
          Thing('m', 'pr', 2),
          Thing('g', 'ru', 2),
          Thing('m', 'ru', 2)]
alreadyVisited = []
addVisited(things, alreadyVisited, 0)
move(0, 0, things, alreadyVisited)
