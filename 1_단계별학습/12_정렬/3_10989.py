'''
문제 팁: 수의 범위가 작다면 카운팅 정렬 사용해 빠르게 정렬
'''
import sys

def count_sort(arr: list, size: int, max: int):
    count = [0 for _ in range(max+1)]
    
    for i in arr:
        count[i] += 1
    
    for idx, i in enumerate(count):
        if i!=0:
            for k in range(i):
                sys.stdout.write(str(idx)+'\n')