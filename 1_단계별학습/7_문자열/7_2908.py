a, b = input().split()
a = int(a[::-1]) # [::-1] 로 역순을 만들 수 있음
b = int(b[::-1])
if a > b:
    print(a)
else:
    print(b)