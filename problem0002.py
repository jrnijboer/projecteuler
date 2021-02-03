a, b, s = 1, 1, 0
while a < 4000000:
    if a % 2 == 0:
        s += a
    a, b = b, b + a
print(s)
