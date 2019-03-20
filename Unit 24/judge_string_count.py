input_string = input().split()

count = 0
for word in input_string:
    if word.strip('.,') == 'the':
        count += 1

print(count)