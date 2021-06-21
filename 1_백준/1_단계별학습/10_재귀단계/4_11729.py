'''
하노이판 옮기기
1. 우선 재귀로 생각 (n개 옮기려면 n-1, n-2, ... , 1)
2. 옮길 때 시작점, 도착점, 거처가는 점으로 구분하기
'''
def hanoi(max: int, start: int, end: int, to: int):
    if max == 1:
        print(start, end) # 가장 큰 하노이판 옮기기
    else:
        hanoi(max-1, start, to, end)
        print(start, end)
        hanoi(max-1, to, end, start)
if __name__ == "__main__":
    n = int(input())
    print(2**n-1)
    hanoi(n, 1, 3, 2)