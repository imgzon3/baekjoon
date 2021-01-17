a, b, c = map(int, input().split()) # 값 받기
# a + b * x < c * x

if b == c:
    print(-1)
else:
    n = a//(c-b)
    if n < 0:
        print(-1)
    else:
        print(n+1)