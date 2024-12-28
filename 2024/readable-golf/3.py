import re
s, on = 0, True
for a,b,do,_ in re.findall("mul[\(](\d+),(\d+)[\)]|(do\(\))|(don't\(\))", open("3.in").read()):
    if a and on: s += int(a)*int(b)
    else: on = bool(do)
print(s)