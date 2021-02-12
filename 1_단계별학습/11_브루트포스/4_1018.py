# 정답 리스트 굳이 만들 필요 없었음
# 조금더 간략화 하기
'''
def chess(m:int, n:int)->int:
    chess_list = [] # 전체 판 리스트 str로 받기
    for _ in range(n):
        tmp = input()
        chess_list.append(list(tmp))
    
    ans_1 = 'WBWBWBWB'
    ans_2 = 'BWBWBWBW'
    answer_1 = [] # 정답 리스트 2개
    answer_2 = []
    
    for i in range(8):
        if i%2 == 0:
            answer_1.append(list(ans_1))
            answer_2.append(list(ans_2))
        else:
            answer_1.append(list(ans_2))
            answer_2.append(list(ans_1))
    
    minimum = 65 # 최솟값
    
    for i in range(m-7):
        for k in range(n-7):
            # answer_1, 2에 따른 칠하는 값
            tmp_1 = 0
            tmp_2 = 0
            for j in range(8):
                for l in range(8):
                    if j%2 == 0:
                        if i%2 == 0:
                            if chess_list[i+j][k+l] == 'W':
                                tmp_2 += 1
                            else:
                                tmp_1 += 1
                        else:
                            if chess_list[i+j][k+l] == 'W':
                                tmp_1 += 1
                            else:
                                tmp_2 += 1
                    else:
                        if i%2 == 0:
                            if chess_list[i+j][k+l] == 'W':
                                tmp_1 += 1
                            else:
                                tmp_2+= 1
                        else:
                            if chess_list[i+j][k+l] == 'W':
                                tmp_2 += 1
                            else:
                                tmp_1 += 1
            tmp = min(tmp_1, tmp_2)
            if tmp < minimum:
                minimum = tmp
    return minimum

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(chess(b, a))
'''

n, m = map(int, input().split())
li = []
mini = []

for _ in range(n):
    li.append(input())

for a in range(n-7):
    for i in range(m-7):
        idx1 = 0
        idx2 = 0
        for b in range(a, a+8):
            for j in range(i, i+8):
                if (j+b)%2 == 0:
                    if li[b][j] != 'W': idx1 += 1
                    if li[b][j] != 'B': idx2 += 1
                else:
                    if li[b][j] != 'W': idx2 += 1
                    if li[b][j] != 'B': idx1 += 1
        mini.append(idx1)
        mini.append(idx2)
print(min(mini))