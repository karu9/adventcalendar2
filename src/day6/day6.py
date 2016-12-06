file = open('input.txt').readlines()
alphabet = "abcdefghijklmnopqrstuvwxyz"
occurences = [[0 for i in range (26)] for i in range(8)]
print(occurences)
for input in file:
    i = 0
    while i < 8 :
        index = alphabet.index(input[i])
        occurences[i][index] += 1
        i+=1
i = 0
#part 1#
while i < 8 :
    print(alphabet[occurences[i].index(max(occurences[i]))], end = '')
    i+=1
print('')
#part 2#
i = 0
while i < 8 :
    print(alphabet[occurences[i].index(min(occurences[i]))], end = '')
    i+=1
