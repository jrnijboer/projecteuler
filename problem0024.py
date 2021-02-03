import itertools
print(''.join(([str(n) for n in (sorted(itertools.permutations(range(10), 10))[999999])])))