from collections import defaultdict
from typing import Generator
import intcode

program = intcode.parse_program(open("input/11.in").read())


def paint_panels(
    computer: Generator[int, int, None], hull: defaultdict[tuple[int, int], int]
) -> defaultdict[tuple[int, int], int]:
    x, y = 0, 0
    dx, dy = 0, -1
    try:
        while True:
            hull[(x, y)] = intcode.input_until_output(computer, hull[(x, y)])
            rotation = next(computer)
            if rotation:
                dx, dy = 0 if dx else -dy, 0 if dy else dx
            else:
                dx, dy = 0 if dx else dy, 0 if dy else -dx
            x += dx
            y += dy

    except StopIteration:
        return hull


p1 = intcode.compute(program.copy())
next(p1)
hull: defaultdict[tuple[int, int], int] = defaultdict(int)
print(f"Part 1: {len(paint_panels(p1, defaultdict(int)).keys())}")

p2 = intcode.compute(program.copy())
next(p2)
hull = paint_panels(p2, defaultdict(int, {(0, 0): 1}))
X, Y = [c[0] for c in hull.keys()], [c[1] for c in hull.keys()]
x0, x1, y0, y1 = min(X), max(X), min(Y), max(Y)
print(f"Part 2:")
for y in range(y0, y1 + 1):
    for x in range(x0, x1 + 1):
        print("\u2588" if hull[(x, y)] else " ", end="")
    print()
