import intcode
import networkx as nx

program = intcode.parse_program(open("input/15.in").read())

GRAPH = nx.Graph()
COMPUTER = intcode.computer(program.copy())
next(COMPUTER)
DIRECTIONS = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
BACKTRACK = {1: 2, 2: 1, 3: 4, 4: 3}


def move_robot(x: int, y: int, V: set[tuple[int]]):
    target = None
    V.add((x, y))
    for command, (dx, dy) in DIRECTIONS.items():
        if (x + dx, y + dy) in V:
            continue
        status = intcode.input_until_output(COMPUTER, command)
        if status == 2:
            target = (x + dx, y + dy)
        if status:
            target = target or move_robot(x + dx, y + dy, V)
            GRAPH.add_edge((x, y), (x + dx, y + dy))
            # Move it back before checking the next path
            intcode.input_until_output(COMPUTER, BACKTRACK[command])
    return target


target = move_robot(0, 0, set())

print(f"Part 1: {nx.shortest_path_length(GRAPH, (0, 0), target)}")

distances = nx.single_source_shortest_path_length(GRAPH, target)
print(f"Part 2: {max(l for l in distances.values())}")
