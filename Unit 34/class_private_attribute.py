class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦

    def pay(self, amount):
        if amount > self.__wallet:    # 사용하려고 하는 금액보다 지갑에 든 돈이 적을 때
            print('돈이 모자라네...')
            return
        self.__wallet -= amount

    def info(self):
        print(self.name, self.age, self.address, self.__wallet)

    def info_wallet(self):
        return self.__wallet

maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(30000)
#maria.info()
print(maria.info_wallet())
