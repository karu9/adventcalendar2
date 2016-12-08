file = open('input.txt').readlines()
screen = [[' ']*50 for i in range(6)]
def createRect(inp):
    for x in range(int(inp[0])):
        for y in range(int(inp[1])):
            screen[y][x] = '♥'
def rotate(inp):
    if 'column' in inp:
        for i in range(inp[2]):
            screen6 = screen[5][inp[1]]
            for y in reversed(range(1,6)):
                screen[y][inp[1]] = screen[y-1][inp[1]]
            screen[0][inp[1]] = screen6
    else :
        for i in range(inp[2]):
            screen50 = screen[inp[1]][49] 
            for x in reversed(range(1, 50)):
                screen[inp[1]][x] = screen[inp[1]][x-1]
            screen[inp[1]][0] = screen50
for input in file:
    splitInput = input.split();
    if 'rect' in splitInput:
        createRect(splitInput[1].split('x'))
    else :
        rotate([splitInput[1], int(splitInput[2].split('=')[1]), int(splitInput[4])])
print (''.join('\n'.join(str(screen)[2:-2].split('], [')).split("', '")))
print(sum(x.count('♥') for x in screen))
