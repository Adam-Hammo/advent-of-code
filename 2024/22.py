from collections import defaultdict
import os
d = [int(x) for x in open(f"input/{os.path.basename(__file__).split('.')[0]}{'s' if os.getenv('TEST')=='Y' else ''}.in").readlines()]

def f(x, n):
    return (x^n)%16777216

signals = defaultdict(dict)
for stream, secret_number in enumerate(d):
    prior_price = secret_number%10
    signal = ""
    for _ in range(2000):
        secret_number = f(secret_number*64, secret_number)
        secret_number = f(secret_number//32, secret_number)
        secret_number = f(secret_number*2048, secret_number)
        price = secret_number%10
        signal += str(f"{price-prior_price:+}")
        if len(signal)>8:
            signal = signal[2:]
        if len(signal)==8 and stream not in signals[signal]:
            signals[signal][stream] = price
        prior_price = price

print(max(sum(streams.values()) for streams in signals.values()))