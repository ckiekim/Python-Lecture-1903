count = int(input('높이를 입력하세요: '))

for i in range(count):
    for k in range(count-1-i):
        print(' ', end='')
    for k in range(2*i+1):
        print('*', end='')
    print()
