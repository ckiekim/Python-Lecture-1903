first, last = map(int, input().split())

answer = []
for i in range(first, last+1):
    if i == first+1 or i == last-1:
        continue
    answer.append(2**i)

print(answer)