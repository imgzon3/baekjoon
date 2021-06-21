import sys

n = int(input())
res = []
for _ in range(n):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a)
    res.append([a, b])

res.sort(key=lambda res:res[0])

for i in res:
    sys.stdout.write(str(i[0])+' '+i[1]+'\n')