def sol(n:int)-> int:
    if n < 10: # 한자리 수라면 생성자가 없다
        return 0
    elif 10 <= n < 20: # 10~19까지 숫자 따로 계산
        if n%2 == 0:
            return int(n/2)
        else:
            return 0
    else:
        lenth = len(str(n)) # 자리 수
        start = n - lenth * 9
        result = 0 # 결과 값
        for i in range(start, n):
            tmp = 0
            for k in str(i):
                tmp += int(k)
            tmp += i
            if tmp == n:
                result = i
                break
        return result

if __name__ == "__main__":
    n = int(input())
    print(sol(n))