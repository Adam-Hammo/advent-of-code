import intcode

program = intcode.parse_program(open("input/13.in").read())
screen = {}

computer = intcode.computer(program.copy())

try:
    while True:
        x, y, tile_id = next(computer), next(computer), next(computer)
        screen[(x, y)] = tile_id
except StopIteration:
    print(f"Part 1: {sum(bool(x==2) for x in screen.values())}")


playable_program = program.copy()
playable_program[0] = 2
computer = intcode.computer(playable_program)
next(computer)
ball_x, paddle_x = None, None
try:
    while True:
        # Our AI will track the position of the ball to move the joystick
        x = intcode.input_until_output(
            computer,
            (
                0
                if (ball_x is None or paddle_x is None or ball_x == paddle_x)
                else -1
                if ball_x < paddle_x
                else 1
            ),
        )
        y, tile_id = next(computer), next(computer)
        if tile_id == 4:
            ball_x = x
        if tile_id == 3:
            paddle_x = x
        if x == -1 and y == 0:
            score = tile_id
        screen[(x, y)] = tile_id
except StopIteration:
    print(f"Part 2: {score}")
