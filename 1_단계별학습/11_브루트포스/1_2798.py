def black(n:int, m:int)-> int:
    cards = list(map(int, input().split()))
    max = 0
    for i in range(n):
        for k in range(i+1, n):
            for l in range(k+1, n):
                tmp = cards[i] + cards[k] + cards[l]
                if max < tmp <= m:
                    max = tmp
    return max

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(black(a, b))