N = 1 * 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
n = N
while True:
    divisible = True
    for i in range(1, 21):
        if n % i != 0:
            divisible= False
            break
    if divisible:
        print(n)
        break
    else:
        n += N
