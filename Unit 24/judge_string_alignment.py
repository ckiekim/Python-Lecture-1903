price_list = list(map(int, input().split(';')))

price_list.sort(reverse=True)
for price in price_list:
    print('%9s' % format(price, ','))

