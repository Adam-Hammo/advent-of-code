import os
from collections import defaultdict
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

# from magic import magic
from graphlib import TopologicalSorter

# Parse
page_rules = defaultdict(set)
pageses = []
mids = []
for l in d:
    if "|" in l:
        X,Y = l.split("|")
        page_rules[int(X)].add(int(Y))
    else :
        n=l.split(",")
        if n == [""]:
            continue
        pageses.append({int(x): i for i, x in enumerate(n)})
        mids.append(int(n[int((len(n)-1)/2)]))

# P1
s = 0
incorrect_pageses = []
for pages, mid in zip(pageses, mids):
    for X,Y in page_rules.items():
        if any(pages.get(X, 0) > pages.get(y, 100) for y in Y):
            incorrect_pageses.append(pages)
            break
    else:
        s += mid
print(s)

# P2
m = 0
for pages in incorrect_pageses:
    # bruh
    sorted_pages = list(TopologicalSorter({X: Y&pages.keys() for X,Y in page_rules.items() if X in pages}).static_order())
    m += sorted_pages[int((len(sorted_pages)-1)/2)]

print(m)