i = int(input())
result = [f'{i} * {j} = {i*j}' for j in list(range(1, 10))]
for r in result:
    print(r)    