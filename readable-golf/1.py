d=open("1.in").read().split("\n")
x=sorted([int(x.split()[0]) for x in d])
y=sorted([int(x.split()[1]) for x in d])
print(sum(abs(a-b) for a,b in zip(x,y)), sum(a*y.count(a) for a in x))