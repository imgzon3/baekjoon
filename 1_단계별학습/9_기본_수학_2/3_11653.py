# '''
# 소인수분해
# 1. 수 받음(n)
# 2. 2~n 까지 소수 나열 (에라토스테네스 체 활용)
# 3. n을 작은 소수부터 나누어 보기, 반복
# 4. 1이 되면 멈춤
# '''

# n = int(input()) # 소인수 분해 할 수

# if n != 1:
#     decimal_bool = [True for i in range(n+1)]

#     for i in range(2, int(n**0.5) + 1): # 남은 수 중 아직 처리하지 않은 i
#         if decimal_bool[i] == True:
#             j = 2
#             while i*j <= n:
#                 decimal_bool[i*j] = False # i의 배수 모두 제거
#                 j += 1

#     decimal = [i for i in range(2, n+1) if decimal_bool[i]] # 소수 리스트

#     left = n
#     while True: # 소인수분해
#         if left == 1: # 더이상 나눌 것이 없다면(1이라면) 끝
#             break
#         for i in decimal:
#             if left%i == 0: # 특정 소수로 나누어지면 출력하고 나누어줌
#                 print(i)
#                 left = left/i
#                 break

# 위에처럼 해도 가능, 그러나 시간 초과 걸림
# 굳이 소수만 제거할 필요 없이, 그냥 순서대로 해도 괜찮을 듯

n = int(input()) # 소인수분해할 수

j = 2 # 나눌 수(소수)
while True:
    if n == 1:
        break
    elif n%j == 0:
        print(j)
        n = n/j
    else:
        j += 1