rows = ['......^.^^.....^^^^^^^^^...^.^..^^.^^^..^.^..^.^^^.^^^^..^^.^.^.....^^^^^..^..^^^..^^.^.^..^^..^^^..']
traps3 = ['.^^','^^.','^..','..^']
traps0 = ['.^','^^']
trapsN = ['^^','^.']
while len(rows) != 400000:
    row = ''
    for i in range(len(rows[0])):
        col = '.'
        previousRow = rows[-1]
        if i == 0:
            if previousRow[:2] in traps0:  
                col = '^'
        elif i == len(rows[0])-1:
            if previousRow[-2:] in trapsN:  
                col = '^'
        elif previousRow[i-1:i+2] in traps3:
            col = '^'
        row += col
    rows.append(row)
print(sum(list(map(lambda x : x.count('.'), rows))))
