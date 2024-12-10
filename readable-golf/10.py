from collections import defaultdict
g,s,e,m=defaultdict(set),set(),set(),[[int(y)for y in x]for x in open("10.in").read().split('\n')]
for y,r in enumerate(m):
    for x,v in enumerate(r):
        if v==0: s.add((x,y))
        if v==9: e.add((x,y))
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            if 0<=y+dy<len(m)and 0<=x+dx<len(r)and m[y+dy][x+dx]==v+1: g[(x,y)].add((x+dx,y+dy))
def t(c): return sum(1 if d in e else t(d) for d in g[c])
print(sum(t(p) for p in s))