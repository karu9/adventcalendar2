inp = '11101000110010100'
inplen = 35651584
print("let's start to create the 'dragon curve'")
while len(inp) < inplen:
    inp += '0' + ''.join(list(map(lambda x : str((int(inp[len(inp) - x - 1]) + 1) % 2), range(len(inp)))))
    completionRate = round(len(inp) * 100 /inplen)
    print(str(completionRate) + '%')
    if completionRate >= 50 and completionRate < 100:
        print("almost There, one more step!")
inp = inp[:inplen]
maxNumberOfStep = 0
while (inplen / 2**maxNumberOfStep) % 2 == 0:
    maxNumberOfStep +=1
print("there will be " + str(maxNumberOfStep) + " steps to get the checksum")
step = 0 
while len(inp) % 2 == 0:
    inp = ''.join(list(map(lambda x: str((abs(int(inp[x]) - int(inp[x+1]))+1) % 2), range(0, len(inp), 2))))
    step += 1
    completionRate = round(step / maxNumberOfStep)
    print(str(completionRate) + '%')
print(inp)
