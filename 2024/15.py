import copy, os
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

def move(x,y,dx,dy,c):
    s = WH[(x+dx,y+dy)]
    if s == "#":
        return x,y
    elif s == ".":
        WH[(x,y)] = "."
        WH[(x+dx,y+dy)] = c
        return x+dx,y+dy
    else:
        _x1,_y1 = move(x+dx,y+dy,dx,dy,s)
        if dy:
            # Move the rest of the box
            _,_y2 = move(x+{"[":1,"]":-1}[s],y+dy,dx,dy,{"[":"]","]":"["}[s])
        else:
            _y2=_y1
        if _x1 == x+dx and (_y1 == y+dy or _y2 == y+dy):
            return x,y
        WH[(x,y)] = "."
        WH[(x+dx,y+dy)] = c
        return x+dx,y+dy

WH = {}
for (_y,row) in enumerate(d):
    if ("#") in row:
        for (_x,c) in enumerate(row):
            if c == "@":
                x,y=_x,_y
            WH[(_x,_y)] = c
        continue
    for c in row:
        _WH, _x, _y = copy.deepcopy(WH), x, y
        dx, dy = {"v": (0,1), "^": (0,-1), ">": (1,0), "<": (-1,0)}[c]
        x,y=move(x,y,dx,dy,"@")
        # Instead of actually solving the problem, just rollback if we dislocated a box
        for (__x,__y) in sorted(WH.keys()):
            if WH[(__x,__y)] == "[" and WH.get((__x+1,__y)) != "]":
                WH, x, y = _WH, _x, _y

print(sum(x+100*y for (x,y),v in WH.items() if v == "["))