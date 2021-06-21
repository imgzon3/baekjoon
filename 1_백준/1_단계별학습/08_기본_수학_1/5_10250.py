num = int(input()) # 테스트 개수
for i in range(num):
    h, w, n = map(int, input().split())
    front = str(n - (n//h)*h)
    back = str(n//h + 1)
    if front == '0': # 옥상 층인 경우
        front = str(h)
        back = str(int(back) - 1)
    if int(back) < 10:
        back = '0' + back
    print(int(front+back))