keys = input().split()
values = map(int, input().split())

x = dict(zip(keys, values))

x.pop('delta')
for key, value in x.items():
    if value == 30:
        found_key = key

x.pop(found_key)
print(x)
