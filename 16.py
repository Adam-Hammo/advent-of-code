import os
import networkx as nx
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

M = {}
for y, row in enumerate(d):
    for x, c in enumerate(row):
        M[(x,y)] = c
        if c == "S":
            S = (x,y)
        if c == "E":
            E = (x,y)

G = nx.Graph()
for (x,y), n in M.items():
    if n in ("S","E","."):
        for dx, dy in ((-1,0),(0,-1),(1,0),(0,1)):
            for _dx, _dy in ((-1,0),(0,-1),(1,0),(0,1)):
                G.add_edge((x,y,dx,dy),(x,y,_dx,_dy),weight=1000)
            if M[(x+dx,y+dy)] in ("S","E","."):
                G.add_edge((x,y,dx,dy),(x+dx,y+dy,dx,dy),weight=1)

cost = min(
    nx.dijkstra_path_length(G, (S[0],S[1],1,0), (E[0],E[1],0,-1)),
    nx.dijkstra_path_length(G, (S[0],S[1],1,0), (E[0],E[1],1,0)),
)

forward = nx.single_source_dijkstra_path_length(G, (S[0],S[1],1,0))
b1, b2 = nx.single_source_dijkstra_path_length(G, (E[0],E[1],1,0)), nx.single_source_dijkstra_path_length(G, (E[0],E[1],0,-1))
backward = {k: min(i for i in (b1.get(k), b2.get(k)) if i is not None) for k in b1.keys() | b2}

V = set()
for node in forward.keys():
    if forward[node] + backward[node] == cost:
        V.add(node[0:2])
print(cost, len(V))
