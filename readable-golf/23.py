import networkx as nx
C = list(nx.enumerate_all_cliques(nx.Graph(x.split("-") for x in open("23.in").read().split("\n"))))
print(sum(1 for c in C if len(c)==3 and any(u[0]=="t" for u in c)), ','.join(sorted(C[-1])))