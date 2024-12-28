import os
s = [list(x) for x in open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")]

def search_dirs(dirs, r, c, i, target):
    new_dirs = {}
    for d, (dr, dc) in dirs.items():
        if 0<=r+i*dr<=len(s)-1 and 0<=c+i*dc<=len(s[r])-1:
            if s[r+i*dr][c+i*dc] == target[i]:
                new_dirs[d] = (dr, dc)
    return new_dirs

p1 = 0
p2 = 0
for r in range(len(s)):
    for c in range(len(s[r])):
        if s[r][c] == "X":
            dirs = {"u": (-1,0), "d": (1,0), "l": (0,-1), "r": (0,1), "ul": (-1,-1), "ur": (-1,1), "dl": (1,-1), "dr": (1,1)}
            dirs = search_dirs(dirs, r, c, 1, "XMAS")
            dirs = search_dirs(dirs, r, c, 2, "XMAS")
            dirs = search_dirs(dirs, r, c, 3, "XMAS")
            p1 += len(dirs)

        if s[r][c] == "A":
            dirs = {"ul": (-1,-1), "ur": (-1,1), "dl": (1,-1), "dr": (1,1)}
            dirs = search_dirs(dirs, r, c, 1, "AMS")
            dirs = search_dirs(dirs, r, c, -1, "AMS")
            if len(dirs) == 2:
                p2 += 1

print(p1, p2)