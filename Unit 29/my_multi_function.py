def my_multi(x):    # list x를 매개변수로 받음
    min = x[0]
    max = x[0]
    sum = 0
    for item in x:
        if min > item:
            min = item
        if max < item:
            max = item
        sum += item
    avg = sum / len(x)

    var = 0
    for item in x:
        var += (item - avg)**2
    var /= len(x)

    return min, max, sum, avg, var

given_list = [9, 12, 3, 45, 87, 34, 67, 91, 55, 41]
min, max, sum, avg, var = my_multi(given_list)
print(min, max, sum, avg, var)

