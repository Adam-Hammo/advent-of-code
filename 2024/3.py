import os
import re
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

m = 0
on = True
for instruction in d:
    r = re.compile("(mul)[(]\d{1,3},\d{1,3}[)]|(do\(\))|(don't\(\))")
    n = 0
    for x in r.finditer(instruction):
        i = x.group()
        if i == "don't()":
            on = False
            continue
        elif i == "do()":
            on = True
            continue
        if on:
            a,b = i.split(",")
            a = int(a.split("(")[1])
            b = int(b[:-1])
            m += a*b

print(m)