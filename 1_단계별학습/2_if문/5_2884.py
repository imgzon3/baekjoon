a, b = map(int, input().split())
if 45 <= b <60:
    print(a, b-45)
elif a != 0 and 0 <= b < 45:
    print(a - 1, 60 - (45-b))
elif a == 0 and 0 <= b < 45:
    print(23, 60 - (45-b))