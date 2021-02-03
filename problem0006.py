sumSquare, squareSum = 0, 0
for i in range(101):
    sumSquare += i * i
    squareSum += i
print(abs(squareSum * squareSum - sumSquare))
