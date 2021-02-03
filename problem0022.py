names = sorted([name.replace('"', '') for name in open("input22.txt").read().split(",")])
def scoreName(name):
    return sum([ord(letter) - ord('A') + 1 for letter in name])
print(sum([(i + 1) * scoreName(name) for i, name in enumerate(names)]))