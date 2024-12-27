import os
schematics = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n\n")

for schematic in schematics:
    structure = schematic.split("\n")
    locks = [s.split("\n") for s in schematics if all(x=="#" for x in s.split("\n")[0])]
    keys = [s.split("\n") for s in schematics if all(x=="." for x in s.split("\n")[0])]

s = 0
for lock in locks:
    for key in keys:
        s += not any(any([a==b=="#" for a,b in zip(l,k)]) for l,k in zip(lock, key))
    
print(s)