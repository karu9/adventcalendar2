inp = 3014603
#create the first iteration#
situation = [i for i in range(1,inp+1)]
cursor = 0 
while len(situation) != 1:
    nextSit = []
    while cursor < len(situation):
        nextSit.append(situation[cursor])
        cursor += 2
    cursor = cursor % len(situation)
    situation = nextSit
print(situation)
