'''
입력되는 수들의 산술평균, 중앙값, 최빈값, 범위 구해야 함
결국 작은 수 부터 큰 수까지 정렬 한번 해야함
'''
import sys

n = int(input())
num = [int(sys.stdin.readline()) for _ in range(n)]

# 산술평균
mean = round(sum(num)/len(num))
print(mean)

# 중앙값
sort_num = sorted(num)
print(sort_num[len(num)//2])

# 최빈값
count = [0]*8001
for i in num:
    count[i+4000] += 1
res = []
for idx, i in enumerate(count):
    if i==max(count):
        res.append(idx-4000)
if len(res)==1:
    print(res[0])
else:
    print(sorted(res)[1])

# 범위
range = max(num) - min(num)
print(range)