import pickle

name = 'james'
age = 19
address = '서울시 강남구 개포동'
scores = {'korean': 91, 'english': 95, 'mathematics': 85, 'science': 82}

with open('james.p', 'wb') as file:    # hello.txt 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
