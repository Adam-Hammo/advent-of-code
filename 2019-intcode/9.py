import intcode

program = intcode.parse_program(open("input/9.in").read())

p1 = intcode.computer(program.copy())
next(p1)
print(f"Part 1: {p1.send(1)}")

p2 = intcode.computer(program.copy())
next(p2)
print(f"Part 2: {p2.send(2)}")
