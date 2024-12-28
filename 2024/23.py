import networkx as nx
import os
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

G = nx.Graph()
for edge in d:
    u,v = edge.split("-")
    G.add_edge(u,v)

s = 0
for clique in nx.enumerate_all_cliques(G):
    if len(clique) == 3:
        if any(x.startswith("t") for x in clique):
            s += 1

print(s)
print(','.join(sorted(clique)))