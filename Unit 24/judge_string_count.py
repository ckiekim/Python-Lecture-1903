import string

input_string = input()
the_count = input_string.count('the')
print(the_count)

ref_input = input_string.strip('.,').split()
print(input_string.strip('.,'))
count = 0
for word in ref_input:
    if word == 'the':
        count += 1

print(count)