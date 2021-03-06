'''
N, M에 따라 수열 작성
'''
import sys

n, m = map(int, input().split())

for i in range(1, n+1):
    if m==1:
        sys.stdout.write(str(i)+'\n')
    else:
        for k in range()