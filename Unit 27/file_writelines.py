lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
others = ['Hello\n', 'Python\n', 'World!\n']

with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)

with open('hello.txt', 'a') as file:
    file.writelines(others)