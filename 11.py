import os
stones = [int(x) for x in open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split()]
cache = {}
def eval_stone(s, b):
    if (s, b) in cache: return cache[(s, b)]
    if b == 0: a = 1
    elif s == 0: a = eval_stone(1, b-1)
    elif len(ss:=str(s))%2 == 0: a = eval_stone(int(ss[:len(ss)//2]), b-1) + eval_stone(int(ss[len(ss)//2:]),b-1)
    else: a = eval_stone(s*2024, b-1)
    cache[(s,b)] = a
    return a
print(sum(eval_stone(s, 75) for s in stones))