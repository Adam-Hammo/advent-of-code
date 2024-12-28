import intcode

program: list[int] = [int(x) for x in open("input/5.in").read().split(",")]

print(f"Part 1: {intcode.compute(program.copy(), 1)}")
print(f"Part 2: {intcode.compute(program.copy(), 5)}")
