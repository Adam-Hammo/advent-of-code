import os
import networkx as nx
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

M = {}
for y, row in enumerate(d):
    for x, c in enumerate(row):
        M[(x,y)] = c
        if c == "S": S = (x,y)
        if c == "E": E = (x,y)

G = nx.Graph()
for (x,y), n in M.items():
    if n in ("S","E","."):
        for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
            if M[(x+dx,y+dy)] in ("S","E","."):
                G.add_edge((x,y),(x+dx,y+dy),weight=1)

PATH = nx.shortest_path(G, S, E)

s = 0
for i, cheat_start in enumerate(PATH[:-100]):
    for j, cheat_end in enumerate(PATH[i+100:]):
        if abs(cheat_start[0]-cheat_end[0]) + abs(cheat_start[1]-cheat_end[1]) <= min(20, j):
            s += 1

print(s)