file = open('input.txt').readlines()
class Thing:
    def __init__(self, typ, pin):
        self.pin = pin
        self.chips  = []
        self.historychips = []
        self.action = []
        self.typ = typ
    def addAction(self, action):
        self.action = action
    def addchip(self, chip):
        self.chips.append(chip)
        self.historychips.append(chip)
        self.chips = sorted(self.chips)
    def canAct(self):
        if self.typ == 'bot' and len(self.chips) == 2:
            return True
        return False
    def act(self, things):
        getThing(things, self.action[5:7]).addchip(self.chips[0])
        getThing(things, self.action[10:12]).addchip(self.chips[1])
        self.chips = []
def getThing(things, inp):
    for thing in things:
        if thing.typ == inp[0] and thing.pin == inp[1]:
            return thing
    thing = Thing(inp[0], inp[1])
    things.append(thing)
    return thing
things = []
for line in file:
    inp = line[:-1].split(' ')
    if 'bot' == inp[0]:
        bot = getThing(things, inp[:2])
        bot.addAction(inp)
        getThing(things, inp[10:12])
    else :
        bot = getThing(things, inp[4:6])
        bot.addchip(int(inp[1]))
acted = True
while acted:
    acted = False
    for thing in things:
        if thing.canAct():
            thing.act(things)
            acted = True
for thing in things:
    print(thing.typ, thing.pin, thing.historychips)
