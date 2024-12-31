import intcode

program = intcode.parse_program(open("input/5.in").read())

p1 = intcode.computer(program.copy())
next(p1)
p1.send(1)
print(f"Part 1: {list(p1)[-1]}")

p2 = intcode.computer(program.copy())
next(p2)
print(f"Part 2: {p2.send(5)}")
