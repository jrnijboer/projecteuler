N = set()
for a in range(2,101):
    for b in range(2,101):
        N.add(a**b)
print(len(N))
