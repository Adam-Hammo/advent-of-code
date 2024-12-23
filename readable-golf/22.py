from collections import defaultdict

def f(n):
    n=((n<<6)^n)&0xFFFFFF
    n=((n>>5)^n)&0xFFFFFF
    return ((n<<11)^n)&0xFFFFFF

S = defaultdict(dict)
for i, n in enumerate([int(x) for x in open("22.in")]):
    p,s = int(n)%10,""
    for _ in range(2000):
        if i not in S[_s:=(s:=s+str(f"{-p+(p:=(n:=f(n))%10):+}"))[-8:]]: S[_s][i]=p

print(max(sum(i.values()) for i in S.values()))