def getCycleLength(i):
    n = 1
    seq = 0
    numerators = []
    remainders = []
    while n > 0:
        if i > n:
            n *= 10
        if n in remainders and n != 0:
            return i, seq, numerators
        numerators.append(n // i)
        remainders.append(n)
        n = n % i
        seq += 1
    return i, seq, numerators

cycles = {k: v for k, v, _ in [getCycleLength(i) for i in range(1, 1000)]}
print(max(cycles, key=lambda k: cycles[k]))
