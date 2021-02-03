from collections import defaultdict
size = 20
D = defaultdict(int)
for n in range(size + 1):
    D[(n, 0)] = 1
    D[(0, n)] = 1
D[(0, 0)] = 0

for row in range(1, size + 1):
    for column in range(1, size + 1):
        D[(row, column)] = D[(row - 1, column)] + D[(row, column - 1)]

# for row in range(size + 1):
#     for column in range(size + 1):
#         print(D[(row,column)], "", end='')
#     print()

print(D[(size, size)])
