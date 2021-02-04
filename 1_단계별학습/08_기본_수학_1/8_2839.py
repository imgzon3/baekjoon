n = int(input()) # 총 킬로그램 입력받음
count = 0

while True:
    if n%5 == 0: # 5로 나누어진다면
        count += n//5
        print(count)
        break
    n -= 3 # 3 빼주기
    count += 1
    if n < 0: # 해당되는 숫자가 아니라면
        print(-1)
        break