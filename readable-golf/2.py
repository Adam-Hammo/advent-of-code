from itertools import combinations

def is_safe(r):
    return tuple(sorted(r)) in (r,r[::-1]) and all(0<abs(x-y)<=3 for x,y in zip(r,r[1:]))

d = [tuple(int(x) for x in r.split()) for r in open("2.in").read().split("\n")]

print(
    sum(is_safe(r) for r in d),
    sum(any(is_safe(c) for c in combinations(r,len(r)-1)) for r in d),
)
