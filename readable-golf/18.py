import networkx as nx
G = nx.grid_2d_graph(71,71)
for b in [(int(x),int(y)) for x,y in [l.split(",") for l in open("18.in").readlines()]]:
    G.remove_node(b)
    if not nx.has_path(G,(0,0),(70,70)): break
print(b)