from pprint import pprint
a = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트
b = []    # 빈 리스트 생성

for i in a:      # 가로 크기를 저장한 리스트로 반복
    row = []    # 안쪽 리스트로 사용할 빈 리스트 생성
    for k in range(i):    # 리스트 a에 저장된 가로 크기만큼 반복
        row.append(0)
    b.append(row)        # 리스트 b에 안쪽 리스트를 추가

pprint(b, indent=4, width=30)
