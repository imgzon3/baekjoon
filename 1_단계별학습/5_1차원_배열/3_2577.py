a = int(input())
b = int(input())
c = int(input())

result = a*b*c

final = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in str(result):
    final[int(i)] += 1
for i in final:
    print(i)