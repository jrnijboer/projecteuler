import math

def getDivisors(n):
    divisors = []
    for i in range(1, 1 + int(math.sqrt(n))):
        if n % i == 0:
            if i * i == n:
                divisors.append(i)
            else:
                divisors.extend([i, n//i])
    return divisors

amicable = set()
D = {i: sum(getDivisors(i)) - i for i in range(10000)}
for k in D:
    if D[k] < 10000 and D[D[k]] == k and k != D[k]:
        amicable = amicable.union({k, D[k]})
print(sum(list(amicable)))
