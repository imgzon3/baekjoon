'''
입력되는 수들의 산술평균, 중앙값, 최빈값, 범위 구해야 함
결국 작은 수 부터 큰 수까지 정렬 한번 해야함
'''
# import sys

# def main():
#     n = int(input())
#     num = []
#     for _ in range(n):
#         num.append(int(sys.stdin.readline()))
    
#     # 순서대로 산술평균, 중앙값, 최빈값, 범위
#     tmp1 = 0
#     tmp2 = 0
#     tmp3 = 0
#     tmp4 = 0
#     for idx, i in enumerate(sorted(num)):
#         tmp1 += i
        
#         if idx == len(num)//2:
#             tmp2 = i
#         elif idx == 0:
#             tmp4 -= i
#         elif idx == len(num)-1:
#             tmp4 += i
#         tmp4 = abs(tmp4)
#     tmp1 = round(tmp1/n)
    
#     count = [0]*8001
#     for i in num:
#         count[i+4000] += 1
    
#     res = []
#     for idx, i in enumerate(count):
#         if i==max(count):
#             res.append(idx-4000)
    
#     if len(res)==1:
#         tmp3 = res[0]
#     else:
#         tmp3 = sorted(res)[1]
    
#     print(tmp1)
#     print(tmp2)
#     print(tmp3)
#     print(tmp4)

# if __name__ == '__main__':
#     main()
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