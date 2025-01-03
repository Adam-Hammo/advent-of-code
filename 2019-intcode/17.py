import intcode

program = intcode.parse_program(open("input/17.in").read())
computer = intcode.computer(program.copy())


def viz(scaffold):
    X, Y = [c[0] for c in scaffold.keys()], [c[1] for c in scaffold.keys()]
    x0, x1, y0, y1 = min(X), max(X), min(Y), max(Y)

    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            print(scaffold[(x, y)], end="")
        print()


def make_scaffold(computer):
    scaffold = {}
    x, y = 0, 0
    for output in computer:
        c = chr(output)
        if c == "\n":
            if not x:
                break
            y += 1
            x = 0
        else:
            scaffold[(x, y)] = c
            x += 1

    return scaffold


scaffold = make_scaffold(computer)

intersections = {
    (x, y)
    for (x, y), v in scaffold.items()
    if v == "#"
    and all(
        (
            scaffold.get((x - 1, y)) == "#",
            scaffold.get((x + 1, y)) == "#",
            scaffold.get((x, y - 1)) == "#",
            scaffold.get((x, y + 1)) == "#",
        )
    )
}
print(f"Part 1: {sum(x * y for (x, y) in intersections)}")

# This was a little bit diagnostic. First I found the simplest traversal:
directions = {"N": (0, -1), "S": (0, 1), "E": (1, 0), "W": (-1, 0)}
direction = "N"
traversal = []
x, y = next((x, y) for (x, y), v in scaffold.items() if v == "^")
while True:
    dx, dy = directions[direction]
    if scaffold.get((x + dx, y + dy)) == "#":
        traversal[-1] += 1
        x += dx
        y += dy
    else:
        # Try turning left
        _direction = {"N": "W", "E": "N", "S": "E", "W": "S"}[direction]
        dx, dy = directions[_direction]
        if scaffold.get((x + dx, y + dy)) == "#":
            traversal.extend(["L", 1])
            x += dx
            y += dy
            direction = _direction
            continue
        # Try turning right
        _direction = {"N": "E", "E": "S", "S": "W", "W": "N"}[direction]
        dx, dy = directions[_direction]
        if scaffold.get((x + dx, y + dy)) == "#":
            traversal.extend(["R", 1])
            x += dx
            y += dy
            direction = _direction
            continue
        break

# print(traversal)

# Because of the way the input is structured, the simple traversal is the segmentable one
# Manually segmented the traversal
A = ["R", "10", "L", "8", "L", "8", "L", "10"]
B = ["L", "8", "R", "10", "L", "10"]
C = ["L", "4", "L", "6", "L", "8", "L", "8"]
routine = ["B", "A", "B", "C", "A", "C", "B", "C", "A", "C"]
M = {"A": A, "B": B, "C": C}

_program = program.copy()
_program[0] = 2
computer = intcode.computer(_program)
scaffold = make_scaffold(computer)
# viz(scaffold)

output = intcode.wait_until_input(computer, ord("\n"))
# print(''.join(chr(x) for x in output))


def send_and_wait_for_next_input(computer, _input):
    next(computer)
    output = []
    for c in ",".join(_input):
        output.append(computer.send(ord(c)))
    output.append(computer.send(ord("\n")))
    output += intcode.wait_until_input(computer, ord("\n"))
    # print(''.join(chr(x) for x in output if x))


send_and_wait_for_next_input(computer, routine)
send_and_wait_for_next_input(computer, A)
send_and_wait_for_next_input(computer, B)
send_and_wait_for_next_input(computer, C)
send_and_wait_for_next_input(computer, ["n"])

print(f"Part 2: {[x for x in computer][-1]}")
