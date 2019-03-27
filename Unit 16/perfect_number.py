
for i in range(1, 10001):
    sum = 0
    for k in range(1, i):
        if i % k == 0:
            sum += k
    if sum == i:
        print(i)

