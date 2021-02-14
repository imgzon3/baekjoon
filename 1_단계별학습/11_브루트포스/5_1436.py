n = int(input())

front = 0 # 앞에 들어가는 숫자
i = 0 # 순서 지정하는 변수
extra = 0 # 앞 숫자에 6 있을 경우, 얼마나 벗어났는지 판단
status = 0# 앞 숫자에 6있을 경우, 상태 판단

if n == 1:
    print(666)
else:
    n -= 1
    for _ in range(n):
        if i == n:
            break
        elif i > n:
            # front -= 1
            extra = status - i + n - 1
            break
        else:
            if (front+1)%1000 == 666:
                i += 1000
                status = 1000
            elif (front+1)%100 == 66:
                i += 100
                status = 100
            elif (front+1)%10 == 6:
                i += 10
                status = 10
            else:
                i += 1
                status = 0
            front += 1

    # print(f'front: {front}, extra: {extra}, status: {status}')
    if status == 0:
        print(str(front)+'666')
    elif status == 10:
        print(str(front)+'66'+str(extra))
    elif status == 100:
        print(str(front)+'6'+str(extra))
    elif status == 1000:
        print(str(front)+str(extra))