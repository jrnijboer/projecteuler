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

n = triangle = 1

while True:
    n += 1
    triangle += n
    if n % 2 == 0:
        cnt = len(getDivisors(n // 2)) * len(getDivisors(n + 1))
    else:
        cnt = len(getDivisors(n)) * len(getDivisors((n + 1) // 2))
    if cnt >= 500:
        print(triangle)
        break
