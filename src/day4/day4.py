file = open('input.txt', 'r').readlines()
alphabet = "abcdefghijklmnopqrstuvwxyz"
sum = 0
for input in file:
    parts = input.split('-')
    name = "".join(parts[:-1])
    sectorId = int(parts[-1][:-8])
    checksum = parts[-1][-7:-2]
    occurences = [0 for i in range(26)]
    for char in name:
        occurences[alphabet.index(char)] += 1
    maxs = sorted(occurences, reverse = True)[:5]
    real = True
    for i in range(5):
        if occurences[alphabet.index(checksum[i])] != maxs[i]:
            real = False
    if real:
        sum += sectorId
print(sum)
