from functools import reduce
blocks = []
m = n = 0
for i, c in enumerate(open("9.in").read()):
    s = int(c)
    if s:
        blocks.append([m, [] if i%2 else [(n, s)], s])
        if i%2<1: n+=1
        m += s
for block in [x for x in blocks[::-1] if len(x[1]) == 1]:
    file = block[1][0]
    if (space := next((y for y in blocks if y[0] < block[0] and y[2] - sum(z[1] for z in y[1]) >= file[1]), None)):
        space[1].append(file)
        block[1].clear()
print(sum(reduce(lambda i, f: (i[0]+f[0]*(f[1]*i[1]+f[1]*(f[1]-1)//2),i[1]+f[1]), B[1], (0, B[0]))[0] for B in blocks))