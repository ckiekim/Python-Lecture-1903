a = [[10, 20, 100], [30, 40], [50, 60, 200, 300]]

for i in range(len(a)):            # 세로 크기
    for k in range(len(a[i])):     # 가로 크기
        print(a[i][k], end=' ')
    print()
