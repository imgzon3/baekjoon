n = int(input()) # 반복 횟수

for _ in range(n):
    x, y = map(int, input().split()) # x좌표, y좌표
    lenth = y - x # 거리 계산
    