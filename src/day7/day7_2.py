file = open('input.txt').readlines()
def returnBAB(inp):
    listBAB = []
    for i in range(len(inp)-2):
        if inp[i] == inp[i+2] and inp[i] != inp[i+1]:
            listBAB.append("".join([inp[i+1], inp[i], inp[i+1]]))
    return listBAB
def hasABABAB(outside, hypernet):
    listBAB = []
    for out in outside:
        listBAB.extend(returnBAB(out))
    hasABABAB = False
    for BAB in listBAB:
        for string in hypernet:
            if BAB in string:
                hasABABAB = True
    return hasABABAB
count = 0
for input in file:
    hypernet = []
    outside = []
    while len(input) != 0:
        if input.startswith('['):
            hypernet.append(input[1:input.index(']')])
            input = input[input.index(']')+1:]
        elif '[' in input:
            outside.append(input[0:input.index('[')])
            input = input[input.index('['):]
        else:
            outside.append(input[:-1])
            input = ''
    if hasABABAB(outside, hypernet):
        count += 1
print(count)
