file = open('input.txt').read()
def decompress(inp) :
    res = ''
    while len(inp) > 0:
        if inp.startswith('('):
            index = inp.index(')')
            marker = inp[1:index].split('x')
            torepeat = inp[index + 1 : int(marker[0]) + index + 1]
            res += torepeat * int(marker[1])
            inp = inp[int(marker[0]) + index +1 :]
        else :
            res += inp[0]
            inp = inp[1:]
    return res
print(len(decompress(file)))
