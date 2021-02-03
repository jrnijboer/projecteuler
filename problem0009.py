def solve():
    for i in range(1, 1000):
        for k in range(i + 1, 1000 - i):
            j = 1000 - (i + k)
            if i * i + j * j == k * k:
                return i * j * k

print(solve())
