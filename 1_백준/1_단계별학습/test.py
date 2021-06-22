def solution(n):
    num = [True for i in range(n+1)] # 0번째 index는 버린다
    num[1] = False # 1은 소수가 아님
    for i in range(1, int(n**0.5)+1):
        if i!=1:
            k=2
            while i*k <= n:
                num[i*k]=False
                k+=1
    result = [i for i in range(2, n+1) if num[i]]
    return len(result)

if __name__=="__main__":
    print(solution(10))