n = int(input())

arr = []
result = []
for _ in range(n): # 숫자 입력 받기
    arr.append(int(input()))

for _ in range(n):
    tmp = min(arr)
    result.append(tmp)
    arr.remove(tmp)

for i in result:
    print(i)