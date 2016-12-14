from hashlib import md5
inp = "qzyelonm"
index = 0
triplets = []
keys = []
def getKey(index):
    hashcount = 1
    key = md5()
    key.update((inp + str(index)).encode('utf-8'))
    key = key.hexdigest()
    while hashcount < 2017:
        currkey = md5()
        currkey.update(key.encode('utf-8'))
        key = currkey.hexdigest()
        hashcount+=1
    return key
while len(keys) < 75:
    key = getKey(index)
    #select only the first triplet#
    r = ''
    for i in range(len(key)-2):
        if key[i] == key[i+1] and key[i] == key[i+2]:
            triplets.append((index, key[i]))
            break
    for i in range(len(key)-4):
        if key[i] == key[i+1] and key[i] == key[i+2] and key[i] == key[i+3] and key[i] == key[i+4]:
            tripletsToRemove = []
            for triplet in triplets:
                if triplet[1] == key[i] and index - triplet[0] <= 1000 and index != triplet[0]:
                    keys.append(triplet)
                    tripletsToRemove.append(triplet)
            for triplet in tripletsToRemove:
                triplets.remove(triplet)
    index += 1
print(sorted(keys)[63])
