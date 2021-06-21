'''
문제 팁: 수의 범위가 작다면 카운팅 정렬 사용해 빠르게 정렬
'''
import sys

def count_sort():
    count = [0 for _ in range(10001)]
    
    n = int(input())
    for i in range(n):
        count[int(sys.stdin.readline())] += 1
    
    for idx, i in enumerate(count):
        for _ in range(i):
            sys.stdout.write(str(idx)+'\n')

if __name__ == '__main__':
    count_sort()