import math
def isPrime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(3, 1 + int(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True

P = [2]
n = 3
while len(P) < 10001:
    if isPrime(n):
        P.append(n)
    n += 2
print(max(P))