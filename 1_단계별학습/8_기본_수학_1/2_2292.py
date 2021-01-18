n = int(input()) # 숫자 입력
# 1 7 19 37
#  6 12 18
#   6  6
total = 1 
plus = 6
count = 1
if n == 1:
    print(1)
else:
    while n >= total:
        total += plus
        plus += 6
        count +=1
    print(count)