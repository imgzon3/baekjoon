num = int(input())
num_list = map(int, input().split())
num_list = list(num_list)
min = num_list[0]
max = num_list[0]
for i in num_list:
    if i < min:
        min = i
    elif i > max:
        max = i
print(min, max)