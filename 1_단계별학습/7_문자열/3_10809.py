import string

asc_list = list(string.ascii_lowercase)
s = input()

# 직접 비교한 경우
# result = ''
# for alp in asc_list:
#     counter = 0
#     for idx, tmp in enumerate(s):
#         if alp == tmp:
#             result += str(idx) + ' '
#             counter = 1
#             break
#     if counter == 0:
#         result += '-1 '

# print(result)

# 구글링 결과, find함수 활용 시
# 더 빠른 값을 구할 수 있었다.
result = ''
for x in asc_list:
    result += str(s.find(x)) + ' '
print(result)