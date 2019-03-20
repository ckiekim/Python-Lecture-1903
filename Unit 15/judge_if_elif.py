age = int(input('나이를 입력하세요> '))
balance = 9000    # 교통카드 잔액

if age < 7:
    print('나이를 다시 입력하세요.')
elif age <= 12:
    balance -= 650
elif age <= 18:
    balance -= 1050
else:
    balance -= 1250

print(balance)
