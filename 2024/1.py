import os
from collections import Counter
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")
l1 = sorted([x.split()[0] for x in d])
l2 = sorted([x.split()[1] for x in d])
d2 = Counter(l2)
print(sum(abs(int(a1)-int(a2)) for a1, a2 in zip(l1, l2)))
print(sum(int(a1)*d2.get(a1, 0) for a1 in l1))