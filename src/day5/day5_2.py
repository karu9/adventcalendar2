import hashlib
input = "uqwqemis"
i = 0
passcode = ["", "", "", "", "", "", "", ""]
while True:
    md5 = hashlib.md5()
    md5.update((input + str(i)).encode('utf-8'))
    hash = str(md5.hexdigest())
    if hash.startswith("00000") :
        try :
            position = int(hash[5])
            if len(passcode[position]) == 0:
                passcode[position] = hash[6]
            else :
                print("value already stored at position: " + hash[5])
            if len("".join(passcode)) == len(passcode):
                print("".join(passcode))
                break;
        except:
            print("not a valid position: " + hash[5])
    i = i + 1
