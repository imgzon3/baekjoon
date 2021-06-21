num = int(input())
c = map(int, input().split())
c = list(c)

max = c[0]
for i in c:
    if i > max:
        max = i

for i in range(len(c)):
    c[i] = (c[i]/max)*100
all = 0
for i in c:
    all += i

print(all/num)