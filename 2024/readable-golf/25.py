S = [c.split("\n") for c in open("25.in").read().split("\n\n")]
print(sum(not any(any(a==b=="#" for a,b in zip(l,k)) for l,k in zip(L,K)) for L in [s for s in S if s[0][0]=="#"] for K in [s for s in S if s[0][0]=="."]))