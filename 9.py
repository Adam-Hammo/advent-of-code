import os
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read()

class File:
    def __init__(self, file_id, size):
        self.file_id = file_id
        self.size = size

    def __repr__(self):
        return str(self.file_id)*self.size

class FSBlock:
    def __init__(self, ix, file_id, size):
        self.ix = ix
        self.files = [File(file_id, size)] if file_id is not None else []
        self.size = size
        
    def remaining_size(self):
        return self.size-sum(f.size for f in self.files)

    def checksum(self):
        n = self.ix
        a = 0
        for file in self.files:
            a += file.file_id * (file.size * n + (file.size * (file.size - 1) // 2))
            n += file.size
        return a

    def __repr__(self):
        return "".join(str(f) for f in self.files) + "."*self.remaining_size()

fs: list[FSBlock] = []
m,n = 0, 0
for i, char in enumerate(d):
    if not (s := int(char)): continue
    if i%2:
        fs.append(FSBlock(m, None, s))
    else:
        fs.append(FSBlock(m, n, s))
        n += 1
    m += s

for i, file_block in enumerate([block for block in fs[::-1] if len(block.files) == 1]):
    file = file_block.files[0]
    try:
        space = next(block for block in fs if block.remaining_size() >= file.size and block.ix < file_block.ix)
        space.files.append(file)
        file_block.files = []
    except StopIteration:
        continue

print(sum(block.checksum() for block in fs))