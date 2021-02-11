# 처음 풀이는 접근방식이 너무 복잡했음
# - 전체적으로 너무 정리하고자 해서, 고려하지 못한 요소들이 너무 많음
# - 따라서 각각 인물마다 다른 인물끼리 비교해서 수가 높다면 +1 하는 방법
'''
def size(n:int)-> list:
    ppl = []
    for i in range(1, n+1):
        tmp = list(map(int, input().split())) # 몸무게, 키 리스트
        tmp.append(i) # 처음 입력된 순서
        ppl.append(tmp)
    
    ppl.sort(key=lambda x : x[0], reverse=True) # 몸무게 순으로 정렬
    # print(f'몸무게 순으로 정렬: {ppl}')
    tmp = 1
    for i in range(n):
        if i == 0: # 가장 큰 몸무게 가진 사람이면
            ppl[i].append(1)
        else:
            if ppl[i][1] >= ppl[i-1][1] or ppl[i][0] == ppl[i-1][0]: # 몸무게 더 큰 사람보다 키가 크다면
                ppl[i].append(ppl[i-1][3])
                tmp += 1
            else: # 몸무게 더 큰 사람보다 키가 작다면
                ppl[i].append(ppl[i-1][3]+tmp)
                tmp = 1
    # print(f'순서 입력된 ppl: {ppl}')
    ppl.sort(key=lambda x: x[2]) # 입력된 순으로 정렬
    # print(f'입력된 순으로 다시 정렬:{ppl}')
    res = []
    for k in ppl:
        res.append(k[3])
    return res

if __name__ == "__main__":
    n = int(input()) # 인원수
    result = size(n)
    res_str = ''
    for idx, i in enumerate(result):
        if idx == len(result)-1:
            res_str += str(i)
        else:
            res_str += str(i) + " "
    print(res_str)
'''

def size(n:int)-> str:
    ppl = []
    for _ in range(n): # 인원 수 만큼 몸무게, 키 받기
        w, h = map(int, input().split())
        ppl.append((w, h))
    
    result = ''
    for idx, i in enumerate(ppl):
        rank = 1 # 기본 rank는 1로 잡기
        
        for k in ppl:
            if i[0]!=k[0] and i[1]!=k[1]: # 본인이 아닌 경우
                if i[0]<k[0] and i[1]<k[1]: # 본인보다 몸무게/키가 큰 경우
                    rank += 1
        
        result += str(rank)
        if idx != n-1:
            result += ' '
    return result
if __name__ == "__main__":
    n = int(input()) # 총 인원수 입력
    print(size(n))