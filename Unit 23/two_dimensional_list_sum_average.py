a = [[10, 20, 100], [30, 40], [50, 60, 200, 300]]

sum = 0
count = 0
min = a[0][0]
max = a[0][0]
for i in range(len(a)):            # 세로 크기
    for k in range(len(a[i])):     # 가로 크기
        sum += a[i][k]
        count += 1
        if min > a[i][k]:
            min = a[i][k]
        if max < a[i][k]:
            max = a[i][k]

print(a)
print(sum, sum/count, min, max)