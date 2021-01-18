a, b, v = map(int, input().split())
# a a-b
days = 1
h = 0
if a >= v:
    print(days)
else:
    h = a
    while h < v:
        h -= b
        days += 1
        h += a
    print(days)