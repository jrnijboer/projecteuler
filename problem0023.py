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

abundant = [i for i in range(1, 28123) if sum(getDivisors(i)) - i > i]

abundantSums = set()
for i in range(len(abundant)):
    for j in range(i, len(abundant)):
        if abundant[i] + abundant[j] <= 28123:
            abundantSums.add(abundant[i] + abundant[j])
        else:
            break
print(sum(set(range(28123)).difference(abundantSums)))
