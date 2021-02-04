n = int(input())
first = 0
second = 1
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    for i in range(n-1):
        tmp = first + second
        first = second
        second = tmp
    print(second)