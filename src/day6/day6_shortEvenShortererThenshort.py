file = open('input.txt').read().replace('\n', '')
alphabet = 'abcdefghijklmnopqrstuvwxyz'
answer = ''
for i in range(8):
    occurence = ''.join(list(map(lambda x : file[x], [j for j in range(len(file)) if j%8 == i])))
    lengths = list(map(lambda x : len(occurence.replace(x, '')), alphabet))
    answer += alphabet[lengths.index(min(lengths))] + alphabet[lengths.index(max(lengths))]
print(''.join(list(map(lambda x : answer[x], [i * 2 for i in range(8)]))) + ',' + ''.join(list(map(lambda x : answer[x], [i * 2 + 1 for i in range(8)]))))
