from functools import lru_cache
@lru_cache(maxsize=1_000_000)
def eval_stone(s,b): return 1 if b==0 else eval_stone(1,b-1) if s==0 else eval_stone(int(str(s)[:len(str(s))//2]),b-1)+eval_stone(int(str(s)[len(str(s))//2:]),b-1) if len(str(s))%2==0 else eval_stone(s*2024,b-1)
print(sum(eval_stone(int(s), 75) for s in open("11.in").read().split()))