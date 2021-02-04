result = []
for i in range(10):
    tmp = int(input())
    tmp = tmp%42
    test = True
    for a in result:
        if a == tmp:
            test = False
    if test == True:
        result.append(tmp)

print(len(result))