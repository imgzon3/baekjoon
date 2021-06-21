'''
N, M에 따라 수열 작성
무조건적으로 for문 늘리기에는 한계
백트래킹이란, DFS 기반으로 불필요한 경우를 배제, 원하는 해답에 도달하는 탐색이다.
'''
# python 내부함수 itertools의 permutations 활용할 시 중복하지 않는 수열을 찾을 수 있다고 함(이래서 내장 함수 꼭 확인)
from itertools import permutations
N, M = map(int, input().split())
P = permutations(range(1, N+1), M)  # iter(tuple)
for i in P:
    print(' '.join(map(str, i)))  # tuple -> str