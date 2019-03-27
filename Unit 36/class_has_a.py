class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        print('안녕하세요.')

class PersonList:
    def __init__(self):
        self.person_list = []    # 리스트 속성에 Person 인스턴스를 넣어서 관리

    def append_person(self, person):    # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)

james = Person('James')
maria = Person('Maria')

plist = PersonList()
plist.append_person(james)
plist.append_person(maria)

print(plist.person_list[0].name)
print(plist.person_list[1].name)