from collections import defaultdict as dd
g=[list(x)for x in open("6.in").read().splitlines()]
R,C=len(g),len(g[0])
m={}
for r in range(R):
    for c,v in enumerate(g[r]):
        m[r,c]=v
        if v=="^": sp=(r,c)
dirs=[(-1,0),(0,1),(1,0),(0,-1)]
loops=0
for r in range(R):
    for c in range(C):
        if m[r,c]!=".": continue
        p,d,V,D=sp,0,set(),dd(set)
        m[r,c]="#"
        while 0<=p[0]<R and 0<=p[1]<C:
            dr,dc=dirs[d]
            np=(p[0]+dr,p[1]+dc)
            if p in V and m.get(np)=="#" and d in D[p]:
                loops+=1
                break
            V.add(p)
            D[p].add(d)
            if m.get(np)=="#": d=(d+1)%4
            else: p=np
        m[r,c]="."
print(loops)