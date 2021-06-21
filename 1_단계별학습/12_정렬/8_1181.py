import sys

n = int(input())
words = []
for _ in range(n):
    words.append(sys.stdin.readline())

tmp = set(words)
words = list(tmp)

# 사전 순서대로 먼저 정렬 후, 단어 개수대로 정렬
words.sort()
words.sort(key=len)

for i in words:
    sys.stdout.write(i)