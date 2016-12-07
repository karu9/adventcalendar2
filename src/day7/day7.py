file = open('input.txt').readlines()
def hasABBA(imp):
    for i in range(len(imp) - 3):
        if imp[i] == imp[i+3] and imp[i+1] == imp[i+2] and imp[i] != imp[i+1]:
            return True
    return False
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
    supportTLS = False
    for string in outside:
        supportTLS |= hasABBA(string)
    for string in hypernet:
        supportTLS &= not hasABBA(string)
    if supportTLS :
        count += 1
print(count)
