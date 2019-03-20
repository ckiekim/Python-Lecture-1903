n = int(input('5자리 정수를 입력하세요> '))
sum = 0
i = 1
while True:
    if (sum > n):
        break
    sum += i
    i += 1
print(i-1, sum-i)