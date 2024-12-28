import intcode

program: list[int] = [int(x) for x in open("input/5.in").read().split(",")]

print(intcode.execute(program, 5))
# print(program)