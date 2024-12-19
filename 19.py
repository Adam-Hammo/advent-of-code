from functools import lru_cache
T, P = (d:=open("19.in").read().split("\n"))[0].split(", "), d[2:]
@lru_cache
def f(p): return sum(f(p[len(t):]) for t in T if p.startswith(t)) if p else 1
print(len([f(p) for p in P if f(p)]), sum(f(p) for p in P))