import intcode
from itertools import permutations

program = intcode.parse_program(open("input/7.in").read())

max_output = 0
for phases in permutations(range(5)):
    phase_computers = {i: intcode.computer(program.copy()) for i in range(5)}
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
    phase_computers = {a: intcode.computer(program.copy()) for a in amplifiers}
    prior_phase_output = 0

    # Instantiate
    for phase in phases:
        next(phase_computers[phase])
        phase_computers[phase].send(phase)

    finished = False
    while not finished:
        for phase in phases:
            try:
                prior_phase_output = intcode.input_until_output(
                    phase_computers[phase], prior_phase_output
                )
            except StopIteration:
                finished = True

    max_output = max(max_output, prior_phase_output)

print(f"Part 2: {max_output}")
