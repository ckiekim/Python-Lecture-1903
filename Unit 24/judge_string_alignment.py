input_list = input().split(';')
price_list = []
for item in input_list:
    price_list.append(int(item))

price_list.sort(reverse=True)
for price in price_list:
    print('%9s' % format(price, ','))

