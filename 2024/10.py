import copy, os
from collections import defaultdict
m = [[int(y) for y in x] for x in open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")]

g = defaultdict(set)
s, e = set(), set()
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == 0:
            s.add((x,y))
        if m[y][x] == 9:
            e.add((x,y))
        for dx, dy in ((-1,0),(1,0),(0,1),(0,-1)):
            if 0<=y+dy<len(m) and 0<=x+dx<len(m[y]) and m[y+dy][x+dx]==m[y][x]+1:
                g[(x,y)].add((x+dx,y+dy))

def find_trails(c,f):
    a = 0
    for c2 in g[c]:
        if c2 in f:
            # f.remove(c2) # uncomment for part 1 lol
            a += 1
        else:
            a += find_trails(c2, f)
    return a

z = 0
for start in s:
    z += find_trails(start,copy.deepcopy(e))

print(z)