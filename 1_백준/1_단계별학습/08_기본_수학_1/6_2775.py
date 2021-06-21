num = int(input()) # 테스트 횟수

for _ in range(num):
    k = int(input()) # k층
    n = int(input()) # n호
    ppl = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            ppl[j] += ppl[j-1]
    print(ppl[-1])