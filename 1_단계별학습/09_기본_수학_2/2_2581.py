'''
에라토스테네스의 체 활용하기
N까지의 소수 확인하려면,

1. 2~N까지 모든 자연수 나열
2. 남은 수 중 아직 처리하지 않은 수 i
3. i의 배수 모두 제거
4. 2, 3 반복 (여기서 i는 N의 제곱근 수 까지라고 한다)
'''

m = int(input()) # m 이상
n = int(input()) # n 이하의 자연수 에서 소수 찾기

num = [True for i in range(n + 1)] # 소수 판단 bool list

for i in range(2, int(n**0.5) + 1): # 남은 수 중 아직 처리하지 않은 i
    if num[i] == True:
        j = 2
        while i*j <= n:
            num[i*j] = False # i의 배수 모두 제거
            j += 1
            
if m == 1:
    m = 2
    
result = [i for i in range(m, n+1) if num[i]] # m, n 사이의 소수 리스트
if len(result) == 0: # 소수가 없을 경우
    print(-1)
else:
    sum = 0
    for i in result:
        sum += i
    # print(result)
    print(sum) # 소수들의 합
    print(result[0]) # 최솟값