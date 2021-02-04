n = int(input())
hansu = 0

for i in range(1, n+1):
    if i < 100:
        hansu += 1
    
    else:
        nums = list(map(int, str(i)))
        if nums[1] - nums[0] == nums[2] - nums[1]:
            hansu += 1
print(hansu)