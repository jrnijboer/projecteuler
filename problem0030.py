S = 0
for i in range(2, 5 * 9 ** 5):
    digits = [int(s) for s in str(i)]
    s = 0
    for j in range(len(digits)):
        s += digits[j]**5
    if s == i:
        S += s

print(S)
