import intcode

program: list[int] = [int(x) for x in open("input/2.in").read().split(",")]

_program = program.copy()
_program[1:3] = [12, 2]

p1 = intcode.compute(_program)
try:
    next(p1)
except StopIteration:
    pass
print(f"Part 1: {_program[0]}")

for noun in range(len(program)):
    for verb in range(len(program)):
        _program = program.copy()
        _program[1:3] = [noun, verb]
        p2 = intcode.compute(_program)
        try:
            next(p2)
        except StopIteration:
            pass
        if _program[0] == 19690720:
            print(f"Part 2: {100*noun+verb}")
