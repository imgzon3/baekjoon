num = int(input())

limit = 10000 # n이 123456까지 입력되므로 그보다 2배 더 큰 값까지 계산

num = [True for i in range(limit + 1)] # 소수 판단 bool list
num[0] = False
num[1] = False
for i in range(2, int(limit**0.5) + 1): # 남은 수 중 아직 처리하지 않은 i
    if num[i] == True:
        j = 2
        while i*j <= limit:
            num[i*j] = False # i의 배수 모두 제거
            j += 1
    
result = [i for i in range(2, limit+1) if num[i]] # limit 까지의 소수 리스트

for _ in num:
    