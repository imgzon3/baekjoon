a, b = map(int, input().split())
c = map(int, input().split())
c = list(c)

result = []
for i in range(a):
    if c[i] < b:
        result.append(c[i])

tmp = ''
for i in result:
    tmp = tmp + str(i) + ' '
print(tmp)