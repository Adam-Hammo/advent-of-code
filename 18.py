import networkx as nx
import os
d = [(int(x),int(y)) for x,y in [l.split(",") for l in open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").readlines()]]
G = nx.Graph({
    (x,y): [(_x,_y) for _x,_y in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)) if 0<=_x<=70 and 0<=_y<=70]
    for x in range(71) for y in range(71)
})
for b in range(len(d)):
    G.remove_node(d[b])
    if not nx.has_path(G,(0,0),(70,70)):
        print(d[b])
        break