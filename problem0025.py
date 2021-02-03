n = 2
fib1 = 1
fib2 = 1
while True:
    next = fib1 + fib2
    fib1 = fib2
    fib2 = next
    n+=1
    if fib2 > 10**(1000-1) :
        print(n)
        break
