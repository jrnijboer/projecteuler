import math
def sieve(n):
    numbers = [True] * n
    sum = 0
    for p in range(2, n):
        for x in range(p * p, n, p):
            numbers[x] = False
    return [i for i, j in enumerate(numbers) if j][2:]

print(sum(sieve(2000000)))
