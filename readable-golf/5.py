from collections import defaultdict
from graphlib import TopologicalSorter
r, ps, a = defaultdict(set), [], defaultdict(int)
for l in open("5.in").read().splitlines():
    if "|" in l: r[int(x := l.split("|")[0])].add(int(l.split("|")[1]))
    elif "," in l: ps.append({int(x): i for i, x in enumerate(l.split(","))})
for p in ps:
    s = tuple(TopologicalSorter({X: Y&p.keys() for X,Y in r.items() if X in p}).static_order())
    a["p2" if any(p.get(x, 0) > p.get(y, 100) for x,Y in r.items() for y in Y) else "p1"] += s[len(s)//2]
print(a)