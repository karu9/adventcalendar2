inp = 3
#create the first iteration#
situation = [i for i in range(1,inp+1)]
cursor = 0
while True:
    toremove = (cursor + round((len(situation)-.1)/2)) % len(situation)
    if cursor == toremove :
        break
    elif cursor < toremove:
        cursor += 1
    else :
        cursor = cursor % len(situation)
    situation.remove(situation[toremove])
print(situation)
