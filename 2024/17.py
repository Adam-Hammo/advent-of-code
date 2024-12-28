from z3 import *

P = [...redacted]
O, x = Optimize(), BitVec('x', 64)
A, B, C = x, 0, 0

for i in P:
    B = A%8
    B ^= 5
    C = A>>B
    B ^= C
    B ^= 6
    A >>= 3
    O.add(B%8==i)

O.add(A==0)
O.minimize(x)
O.check()
print(O.model().eval(x))