file = open('input.txt').readlines()
alphabet = "abcdefghijklmnopqrstuvwxyz"
columns = ['']*8
for input in file:
    for i in range(8):
        columns[i] += input[i]
responses = ['']*2
for i in range(8):
    lenghts = list(map(lambda x : len(columns[i].replace(x, '')), alphabet))
    responses[0] += alphabet[lenghts.index(min(lenghts))]
    responses[1] += alphabet[lenghts.index(max(lenghts))]
print(responses)
