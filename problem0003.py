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

print(max([i for i in range(1, int(math.sqrt(600851475143))) if 600851475143 % i == 0 and isPrime(i)]))
