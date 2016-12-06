import hashlib
input = "uqwqemis"
i = 0
passcode = ""
while True:
    md5 = hashlib.md5()
    md5.update((input + str(i)).encode('utf-8'))
    hash = str(md5.hexdigest())
    if hash.startswith("00000") :
        passcode = passcode + hash[5]
        if len(passcode) == 8:
            print(passcode)
            break;
    i = i + 1
