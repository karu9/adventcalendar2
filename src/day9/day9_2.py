import time
start_time = time.time()
file = open('input.txt').read()
def decompress(inp) :
    if inp.startswith('('):
        index = inp.index(')')
        marker = inp[1:index].split('x')
        torepeat = inp[index + 1 : int(marker[0]) + index + 1]
        torepeatcount = decompress(torepeat)
        return torepeatcount * int(marker[1]) + decompress(inp[int(marker[0]) + index +1 :])
    elif '(' in inp :
        index = inp.index('(')
        return len(inp[:index]) + decompress(inp[index:])
    else :
        return len(inp)
print(decompress(file))
print("--- %s seconds ---" % (time.time() - start_time))
