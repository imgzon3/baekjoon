count = int(input())
for i in range(count):
    tmp = input()
    score = 0
    stack = 0
    for k in range(len(tmp)):
        if tmp[k] == 'O':
            score += 1 + stack
            stack += 1
        else:
            stack = 0
    print(score)