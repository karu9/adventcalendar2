lines = open('input.txt', 'r').readlines()
registersNames = 'abcd'
registers = [0,0,1,0]
line = 0
while line != len(lines):
    instruction = lines[line][0:-1].split(' ')
    if instruction[0] == 'inc':
        registers[registersNames.index(instruction[1])] += 1
        line += 1
    elif instruction[0] == 'dec':
        registers[registersNames.index(instruction[1])] -= 1
        line += 1
    elif instruction[0] == 'cpy':
        if instruction[1] in registersNames:
            registers[registersNames.index(instruction[2])] = registers[registersNames.index(instruction[1])]
        else:
            registers[registersNames.index(instruction[2])] = int(instruction[1])
        line += 1
    else :
        if instruction[1] in registersNames:
            if registers[registersNames.index(instruction[1])] != 0:
                line += int(instruction[2])
            else:
                line += 1
        else :
            if int(instruction[1]) != 0:
                line += int(instruction[2])
            else:
                line += 1
print(registers)
