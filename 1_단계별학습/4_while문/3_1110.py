inp = int(input())
tmp = inp
result = 0

while(True):
    if tmp >= 10:
        a = int(str(tmp)[1])
        b = int(str(tmp)[0]) + int(str(tmp)[1])
    else:
        a = int(str(tmp)[0])
        b = 0 + int(str(tmp)[0])
    
    if b >= 10:
        b = int(str(b)[1])
    
    tmp = int(str(a) + str(b))

    result += 1
    if tmp == inp:
        break
print(result)