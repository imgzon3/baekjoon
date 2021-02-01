m = int(input())
n = int(input()) # m 이상n 이하의 자연수 에서 소수 찾기

num = [True for i in range(n + 1)] # 소수 판단 bool list

for i in range(2, int(n**0.5) + 1): # 남은 수 중 아직 처리하지 않은 i
    if num[i] == True:
        j = 2
        while i*j <= n:
            num[i*j] = False # i의 배수 모두 제거
            j += 1
            
result = [i for i in range(2, n+1) if num[i]] # m, n 사이의 소수 리스트

print(len(result))