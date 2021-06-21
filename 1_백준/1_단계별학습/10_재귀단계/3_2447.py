# 답은 맞으나, 백준은 numpy를 지원하지 않는다
'''
import numpy as np

def stars(num:int, x:np)->np:
    """[별찍기 재귀함수]

    Args:
        num (int): [패턴의 크기]
        np (x): [초기 문자]
    """
    if num == 1:
        return x
    else:
        tmp = np.full(x.shape, 0)
        
        one = np.append(x, x, axis=1)
        one = np.append(one, x, axis=1)
        two = np.append(x, tmp, axis=1)
        two = np.append(two, x, axis=1)
        res = np.append(one, two, axis=0)
        res = np.append(res, one, axis=0)
        # print(res)
        return stars(int(num**0.5), res)

if __name__ == "__main__":
    n = int(input())
    a = np.full((1, 1), 1)
    result = stars(n, a) # 별 찍힌 곳은 1, 빈칸은 0
    for i in result:
        line = ''
        for k in i:
            if k == 1:
                line += '*'
            elif k == 0:
                line += ' '
        print(line)
'''

# numpy없이
def star(n: int, x: list)-> list:
    out = [] # 한번 처리한 값
    if n == 3:
        return x
    else:
        for i in x: # 위에 처음 3개의 구역
            out.append(i*3)
        for i in x: # 가운데 3개의 구역 (중앙 비어있음)
            out.append(i+' '*len(x)+i)
        for i in x: # 마지막 3개의 구역
            out.append(i*3)
        return star(n//3, out)

if __name__ == "__main__":
    n = int(input())
    first = ['***', '* *', '***']
    final = star(n, first)
    for i in final:
        print(i)