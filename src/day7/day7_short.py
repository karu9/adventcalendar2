import re
file = open('input.txt').readlines()
supernetPattern = r'(?:^|])(?:\w*)(\w)(?!\1)(\w)\2\1(?:\w*)(?:\[|$)'
hypernetPattern = r'(?:\[)(?:\w*)(\w)(?!\1)(\w)\2\1(?:\w*)(?:])'
count = 0
for input in file:
    supernet = re.search(supernetPattern, input)
    hypernet = re.search(hypernetPattern, input)
    if hypernet:
        print("not a TLS")
    elif supernet:
        count += 1
print(count)
