n = int(input())

tmp = 0
tmp_2 = 0
status = 0 # 0이면 일반, 10이면 6, 100이면 66, 1000이면 666
for _ in range(n):
    if tmp == n:
        break
    elif tmp > n:
        tmp_2 = tmp - status
        
    else:
        if tmp%1000 == 666:
            tmp += 1000
            status = 1000
        elif tmp%100 == 66:
            tmp += 100
            status = 100
        elif tmp%10 == 6:
            tmp += 10
            status = 10
        else:
            status = 0
            tmp += 1

print(f'tmp:{tmp}, tmp_2:{tmp_2}')