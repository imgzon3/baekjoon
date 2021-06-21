import sys

n = int(input())
dots = []
for _ in range(n):
    dots.append(list(map(int, sys.stdin.readline().split())))

dots.sort(key=lambda x:(x[1], x[0]))
for i in dots:
    sys.stdout.write(str(i[0])+' '+str(i[1])+'\n')