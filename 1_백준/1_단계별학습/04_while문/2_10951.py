a = 1
b = 1
while(True):
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break