import intcode

program: list[int] = [int(x) for x in open("input/2.in").read().split(",")]

_program = program.copy()
_program[1:3] = [12, 2]

intcode.compute(_program)
print(f"Part 1: {_program[0]}")

for noun in range(len(program)):
    for verb in range(len(program)):
        _program = program.copy()
        _program[1:3] = [noun, verb]
        intcode.compute(_program)
        if _program[0] == 19690720:
            print(f"Part 2: {100*noun+verb}")
