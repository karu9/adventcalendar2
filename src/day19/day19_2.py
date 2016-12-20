inp = 3014603
elfs = []
#create the first iteration#
class Elf :
    def __init__(self, id):
        self.id = id
        self.nextElf = None
        self.previousElf = None
    def delete(self):
        self.previousElf.nextElf = self.nextElf
        self.nextElf.previousElf = self.previousElf
elfs = [Elf(i) for i in range(inp)]
for i in range(inp):
    elfs[i].nextElf = elfs[(i+1)%inp]
    elfs[i].previousElf = elfs[(i-1)%inp]
elf = elfs[0]
toremove = elfs[round((len(elfs)-0.1) / 2)]
for i in range(inp - 1):
    toremove.delete()
    toremove = toremove.nextElf
    if (inp - i) % 2 == 1:
        toremove = toremove.nextElf
    elf = elf.nextElf
print(elf.id+1, elf.nextElf.id+1, elf.previousElf.id+1)
    
