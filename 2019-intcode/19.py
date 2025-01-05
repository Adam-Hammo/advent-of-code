import intcode

program = intcode.parse_program(open("input/19.in").read())


def check_coords(x, y):
    computer = intcode.computer(program.copy())
    next(computer)
    computer.send(x)
    return computer.send(y)


print(f"Part 1: {sum(check_coords(x, y) for x in range(50) for y in range(50))}")

x = y = 0
while not check_coords(x + 99, y):
    y += 1
    while not check_coords(x, y + 99):
        x += 1

print(f"Part 2: {10000*x + y}")
