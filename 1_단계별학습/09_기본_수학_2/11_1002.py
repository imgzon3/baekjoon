n = int(input()) # 반복 횟수
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split()) # 값 입력받음
    lenth = ((x1 - x2)**2 + (y1 - y2)**2)**0.5 # 점 사이의 거리
    # print(f'lenth: {lenth}')
    
    # 원의 중심이 같을 경우
    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        # 한 원이 다른 원 안에 들어갈 경우
        if lenth < abs(r1-r2):
            print(0)
        # 안에서 두 원이 한 점에서 접할 경우
        elif lenth == abs(r1-r2):
            print(1)
        # 두 원이 서로 겹치는 경우
        elif lenth < (r1+r2):
            print(2)
        # 밖에서 두 원이 한 점에서 접할 경우
        elif lenth == (r1+r2):
            print(1)
        # 두 원이 서로 겹치지 않는 경우
        elif lenth > r1 + r2:
            print(0)