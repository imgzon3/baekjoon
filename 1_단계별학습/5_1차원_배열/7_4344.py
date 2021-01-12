num = int(input())
for i in range(num):
    n = map(int, input().split())
    n = list(n)
    avg = 0
    for k in range(1, len(n)):
        avg += n[k]
    avg = avg // n[0]
    
    count = 0
    for k in range(1, len(n)):
        if n[k] > avg:
            count += 1
    
    print('{:.3f}%'.format(count/n[0]*100))