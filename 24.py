import os
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read()

# Solved this one piecemeal - below is diagnostic/iterative/a mess.
# SWAPS = {"z11": "wpd", "jqf": "skh", "z19": "mdd", "z37": "wts"}
# SWAPS |= {v: k for k,v in SWAPS.items()}
SWAPS = {}

wires, gates = d.split("\n\n")
wires = {wire: int(value) for wire, value in [w.split(": ") for w in wires.split("\n")]}
gate_operations = []
for gate in gates.split("\n"):
    operation, output = gate.split(" -> ")
    input1, operator, input2 = operation.split()
    for wire in (input1, input2, output):
        if wire not in wires: 
            wires[wire] = None
    gate_operations.append([input1, operator, input2, SWAPS.get(output, output)])

_wires = None
while _wires != wires:
    _wires = wires.copy()
    for input1, operator, input2, output in gate_operations:
        if wires[input1] is not None and wires[input2] is not None:
            wires[output] = int(eval(f"wires['{input1}'] {'!=' if operator=='XOR' else operator.lower()} wires['{input2}']"))

W = sorted(wires.items(), reverse=True)
x = eval("0b"+"".join(str(v) for w,v in W if w[0]=="x"))
y = eval("0b"+"".join(str(v) for w,v in W if w[0]=="y"))
z = eval("0b"+"".join(str(v) for w,v in W if w[0]=="z"))

# Pwetty Pwintings
width = len(f"{max(x, y, z, x + y, (x + y) & ~z):b}")
print(f"{'x':<12} = {x:>{width}b}")
print(f"{'y':<12} = {y:>{width}b}")
print(f"{'z':<12} = {z:>{width}b}")
print(f"{'(x+y)':<12} = {(x+y):>{width}b}")
print(f"{'(x+y)^z':<12} = {((x+y)^z):>{width}b}")

check = (x + y) ^ z
i = 0
while check:
    if check & 1: print(f"{i}th bit needs fixing")
    check >>= 1
    i += 1

print(",".join(sorted(SWAPS.keys())))