n = int(input())
dots = []
for _ in range(n):
    dots.append(list(map(int, input().split())))

for i in sorted(dots):
    print(i[0], end=' ')
    print(i[1])