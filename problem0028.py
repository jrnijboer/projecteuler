delta = 2
corners = [3, 5, 7, 9]
while delta < 1000:
    last = corners[len(corners) - 1]
    delta += 2
    for i in range(4):
        last += delta
        corners.append(last)

print(sum(corners) + 1)
