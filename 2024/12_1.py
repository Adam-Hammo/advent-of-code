import os
d = {(x,y): c for y,r in enumerate(open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in")) for x,c in enumerate(r.rstrip('\n'))}
v = set()

def p1(x,y,p):
    if (x,y) in v: return 0, 0
    v.add((x,y))
    a = 1
    b = 0
    for (dx,dy) in ((-1,0),(1,0),(0,-1),(0,1)):
        if (q:=d.get((x+dx,y+dy))) and q==p:
            a, b = map(sum, zip((a, b), p1(x+dx, y+dy, p)))
            continue
        else:
            b += 1
    return a, b

def p2(x,y,p):
    if (x,y) in v: return 0, 0
    v.add((x,y))
    a = 1
    b = 0
    for (dx,dy) in ((-1,0),(1,0),(0,-1),(0,1)):
        if (q:=d.get((x+dx,y+dy))) and q==p:
            a, b = map(sum, zip((a, b), p1(x+dx, y+dy, p)))
            continue
        else:
            b += 1
    return a, b

c = 0
for (x,y),p in d.items():
    a,b = p1(x,y,p)
    c += a*b
print(c)