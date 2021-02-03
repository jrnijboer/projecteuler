import math
import itertools

def sieve(n):
    numbers = [True] * n
    sum = 0
    for p in range(2, n):
        for x in range(p * p, n, p):
            numbers[x] = False
    return [i for i, j in enumerate(numbers) if j][2:]

ab = sieve(1000)
ab.extend([-p for p in ab])
P = sieve(1000)
max_sequence = 0
prod = 0
combinations = list(itertools.permutations(ab, 2))

for a, b in combinations:
    seq = 0
    n = 0
    while n * n + a * n + b in P:
        seq += 1
        n += 1
    if seq > max_sequence:
        prod = a * b
        max_sequence = seq

print(prod)
