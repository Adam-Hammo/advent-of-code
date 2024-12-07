import os
s = [list(x) for x in open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")]

d = "u"
ds = {"u": (-1, 0), "l": (0,-1), "d": (1,0), "r": (0,1)}
nd = {"u": "r", "r": "d", "d": "l", "l": "u"}

m = {}
for r in range(len(s)):
    for c in range(len(s[r])):
        if s[r][c] == "^":
            sp = (r,c)
        m[(r,c)] = s[r][c]

from collections import defaultdict
loops = 0
for nr in range(len(s)):
    for nc in range(len(s[nr])):
        print(nr,nc)
        if m[(nr, nc)] != ".":
            continue

        p = sp
        d = 'u'
        visited = set()
        md = defaultdict(set)

        m[(nr,nc)] = "#"
        while 0<=p[0]<len(s) and 0<=p[1]<len(s[0]):
            
            dr, dc = ds[d]
            np = (p[0]+dr, p[1]+dc)
            if p in visited and m[np] == "#" and d in md[p]:
                # print(p)
                loops += 1
                break
        
            visited.add(p)
            md[p].add(d)
            try:
                if m[np] == "#":
                    d = nd[d]
                    continue
            except Exception as e:
                break

            p = np
        
        m[(nr,nc)] = "."


print(len(visited))
print(loops)