import copy, os
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")

n = 0
for row in [[int(x) for x in d.split()] for d in d]:
    increasing = True
    decreasing = True
    safe_gap = True
    for i1 in range(len(row)-1):
        i2=row[i1+1]
        i1=row[i1]
        if i2>i1:
            decreasing = False
        if i2<i1:
            increasing = False
        if abs(i2-i1) > 3 or i2==i1:
            safe_gap = False
    
    if int((increasing or decreasing) and safe_gap):
        n+=1
        continue
    
    for i in range(len(row)):

        increasing = True
        decreasing = True
        safe_gap = True
        new_row = copy.deepcopy(row)
        new_row.pop(i)
        for i1 in range(len(new_row)-1):
            i2=new_row[i1+1]
            i1=new_row[i1]
            if i2>i1:
                decreasing = False
            if i2<i1:
                increasing = False
            if abs(i2-i1) > 3 or i2==i1:
                safe_gap = False
            
        if int((increasing or decreasing) and safe_gap):
            n+=1
            break
    
print(n)