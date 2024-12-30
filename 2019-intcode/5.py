import intcode

program: list[int] = [int(x) for x in open("input/5.in").read().split(",")]

p1 = intcode.compute(program.copy())
next(p1)
p1.send(1)
print(f"Part 1: {list(p1)[-1]}")

p2 = intcode.compute(program.copy())
next(p2)
print(f"Part 2: {p2.send(5)}")
