n = int(input()) # 주어지는 수 개수
a:list = list(map(int, input().split()))
count = len(a)

for i in a:
    if i != 1:
        for k in range(2, i):
            if i%k == 0: # 1 이외에 나누어지는 것이 있다면
                count -= 1
                break
    else:
        count -= 1

print(count)