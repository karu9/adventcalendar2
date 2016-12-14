from hashlib import md5
inp = "ngcjuoqr"
index = 0
keys = []
def getKey(index):
    key = md5()
    key.update((inp + str(index)).encode('utf-8'))
    return key.hexdigest()
while len(keys) < 75:
    key = getKey(index)
    #select only the first triplet#
    possibleKey = ''
    for char in key:
        if char*3 in key:
            possibleKey = char
    if len(possibleKey) != 0:
        for i in range(1,1001):
            kkey = getKey(index + i)
            if possibleKey*5 in kkey:
                keys.append((index, key))
    index += 1
print(sorted(keys)[63])
