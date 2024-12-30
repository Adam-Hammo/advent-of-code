import intcode
from itertools import permutations

program: list[int] = [int(x) for x in open("input/7.in").read().split(",")]

max_output = 0
for phases in permutations(range(5)):
    phase_computers = {i: intcode.compute(program.copy()) for i in range(5)}
    for phase in phases:
        next(phase_computers[phase])
        phase_computers[phase].send(phase)

    prior_phase_output = 0
    for phase in phases:
        prior_phase_output = phase_computers[phase].send(prior_phase_output)

    max_output = max(max_output, prior_phase_output)

print(f"Part 1: {max_output}")

max_output = 0
amplifiers = (5, 6, 7, 8, 9)
for phases in permutations(amplifiers):
    phase_computers = {a: intcode.compute(program.copy()) for a in amplifiers}
    prior_phase_output = 0

    # Instantiate
    for phase in phases:
        next(phase_computers[phase])
        phase_computers[phase].send(phase)

    finished = False
    while not finished:
        for phase in phases:
            try:
                _prior_phase_output = phase_computers[phase].send(prior_phase_output)
                while _prior_phase_output is None:
                    _prior_phase_output = phase_computers[phase].send(
                        prior_phase_output
                    )
                prior_phase_output = _prior_phase_output
            except StopIteration:
                finished = True

    max_output = max(max_output, prior_phase_output)

print(f"Part 2: {max_output}")
