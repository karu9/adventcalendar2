file = open('input.txt').readlines()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
columns = ['']*8
for input in file:
    for i in range(8):
        columns[i] += input[i]
answer = ''
for i in range(8):
    lenghts = list(map(lambda x : len(columns[i].replace(x, '')), alphabet))
    answer += alphabet[lenghts.index(min(lenghts))] + alphabet[lenghts.index(max(lenghts))]
print(''.join(list(map(lambda x : answer[x], [i * 2 for i in range(8)]))) + ',' + ''.join(list(map(lambda x : answer[x], [i * 2 + 1 for i in range(8)]))))
