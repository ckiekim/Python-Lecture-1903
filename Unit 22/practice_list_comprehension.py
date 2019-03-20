a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
#b = [i for i in a if len(i) == 5]
b = []
for i in a:
    if len(i) == 5:
        b.append(i)
print(b)

