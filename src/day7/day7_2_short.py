import re
file = open('input.txt').readlines()
pattern = r'(?:^|])(?:\w*)(\w)(?!\1)(\w)\1(?:\w*)(?:\[|$)'
hypernetPattern = r''
count = 0
for input in file:
    match = re.search(pattern, input)
    if match:
        count += 1
print(count)
