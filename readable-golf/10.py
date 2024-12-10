from collections import defaultdict
g,m=defaultdict(set),[[int(y)for y in x]for x in open("10.in").read().split('\n')]
for y,r in enumerate(m):
    for x,v in enumerate(r):
        for dx,dy in [(-1,0),(1,0),(0,1),(0,-1)]:
            if 0<=y+dy<len(m)and 0<=x+dx<len(r)and m[y+dy][x+dx]==v+1: g[(x,y)].add((x+dx,y+dy))
def t(x,y): return sum(1 if m[y][x]==9 else t(x,y) for x,y in g[(x,y)])
print(sum(t(x,y) for x,y in set(g.keys()) if m[y][x]==0))