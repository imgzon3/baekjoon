word = input().upper() # 숫자 입력, 대문자 화
nums = [] # 알파벳 개수 저장 list
for i in set(word): # unique한 알파벳만
    nums.append(word.count(i)) # 개수 저장

# 최대 빈도수인 알파벳 위치 구하기
idx = [i for i, x in enumerate(nums) if x==max(nums)]
if len(idx) > 1:print('?') # 최대 빈도수 알파벳 2개 이상일 경우
else: print(list(set(word))[idx[0]]) # 아닐 경우