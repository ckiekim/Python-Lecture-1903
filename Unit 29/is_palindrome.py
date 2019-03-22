def is_palindrom(word):     # word는 list 형태
    for i in range(len(word)//2):
        if (word[i] != word[-1-i]):
            return False
    return True

word = input('단어를 입력하세요: ')
print(word, is_palindrom(word.lower()))