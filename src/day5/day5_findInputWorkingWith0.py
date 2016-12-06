import hashlib
import random
alphabet = "abcdefghijklmnopqrstuvwxyz"
while True:
    input = ''
    while True :
        input += alphabet[random.randint(0, 25)]
        if len(input) == 8:
            break
    md5 = hashlib.md5()
    md5.update((input + "0").encode('utf-8'))
    hash = str(md5.hexdigest())
    if hash.startswith("00000") :
        print(input)
