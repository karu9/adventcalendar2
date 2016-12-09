file = open('input.txt').read()
count = 0
def decompress(inp) :
    res = ''
    while len(inp) > 0:
        if inp.startswith('('):
            index = inp.index(')')
            marker = inp[1:index].split('x')
            torepeat = inp[index + 1 : int(marker[0]) + index + 1]
            res += torepeat * int(marker[1])
            inp = inp[int(marker[0]) + index +1 :]
        elif '(' in inp :
            index = inp.index('(')
            res += inp[:index]
            inp = inp[index:]
        else :
            res += inp
            inp = ''
    return res
res1 = decompress(file)
print(len(res1))
res2 = decompress(res1)
while '(' in res2 :
    print(len(res2))
    res2 = decompress(res2)
print(len(res2))
