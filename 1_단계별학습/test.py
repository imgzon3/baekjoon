n = int(input())

tmp = 0 # tmp
tmp_2 = 0 # 6관련된 것이면, 몇번 째 수인지
result = 0 # 앞에 나오는 수
status = 0 # 0이면 일반, 10이면 6, 100이면 66, 1000이면 666
for i in range(n):
    if tmp == n:
        result = i
        break
    elif tmp > n:
        result = i
        tmp_2 = status - tmp + n
        break
    else:
        print(tmp)
        if i%1000 == 666:
            tmp += 1000
            status = 1000
        elif i%100 == 66:
            tmp += 100
            status = 100
        elif i%10 == 6:
            tmp += 10
            status = 10
        elif i == 6:
            tmp += 10
            status = 10
        else:
            status = 0
            tmp += 1

print(f'result:{result}, tmp_2:{tmp_2}')