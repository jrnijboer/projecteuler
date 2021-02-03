SEEN = {}
def collatz(n):
    length = 0
    collatz = n
    while n != 1:
        if n in SEEN:
            SEEN[collatz] = length + SEEN[n]
            return length + SEEN[n]
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        length += 1
    SEEN[collatz] = length
    return length

print(max([(i, collatz(i)) for i in range(1, 1000000)], key = lambda x: x[1])[0])
