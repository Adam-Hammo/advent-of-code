import os
d = open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").read().split("\n")