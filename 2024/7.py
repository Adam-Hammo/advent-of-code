import os
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

from itertools import product

operators, s = {"+", "*", "||"}, 0
for i,l in enumerate(d):
    ans, variables = l.split(": ")
    variables = variables.split(" ")
    n = len(variables)
    for ops in product(operators, repeat=n-1):
        equation = variables[0]
        for i in range(n-1):
            if ops[i] == "||":
                equation = f"{eval(equation)}{variables[i+1]}"
            else:
                equation = f"({equation}{ops[i]}{variables[i+1]})"
        if eval(equation) == int(ans):
            s += int(ans)
            break

print(s)