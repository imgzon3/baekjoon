result = int(input()) # 반복될 단어 개수이자, result값
for i in range(result):
    word = input() # 단어 입력 받기
    for w in range(1, len(word)):
        # 앞 글자가 처음 등장하는 인덱스 보다
        # 뒷 글자가 처음 등장하는 인덱스가 작은 경우
        # 즉, 뒷 글자가 앞 글자보다 먼저 등장했던 경우
        if word.find(word[w-1]) > word.find(word[w]):
            result -= 1 # 그런 글자는 그룹 단어가 아니다
            break

print(result)