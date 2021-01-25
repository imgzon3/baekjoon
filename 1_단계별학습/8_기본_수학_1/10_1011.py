'''
1 + 2 + ... + n-1 + n + n-1 + ... + 2 + 1
이 합은 n**2임
1. 따라서 주어진 길이에서 n**2만큼 빼주고
2. 남은 값은 n보다 작거나 같은 수로 빼주면 될듯
'''

n = int(input()) # 반복 횟수

for _ in range(n):
    x, y = map(int, input().split()) # x좌표, y좌표
    lenth = y - x # 거리 계산
    test = 0 # 장치 작동 횟수
    n = 1 # 위 주석에서 언급한 n
    while n**2 <= lenth:
        n += 1
    n -= 1
    test += 2*n - 1 # n만큼 횟수 추가
    lenth -= n**2 # n**2만큼 뺀 나머지
    
    while True:
        if lenth == 0: # 다 끝난 경우
            print(test)
            break
        elif lenth >= n:
            lenth -= n
            test += 1
        else: # lenth < n
            lenth = 0
            test += 1