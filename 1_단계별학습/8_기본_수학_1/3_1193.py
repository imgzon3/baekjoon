n = int(input())
level, key = 1, 1
while key + level <= n:
    key += level
    level += 1
step = n - key
x, y = step + 1, level - step
if level % 2 == 0:
    print(f'{x}/{y}')
else:
    print(f'{y}/{x}')