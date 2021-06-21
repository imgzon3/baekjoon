a = input()
cro_list = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0 # 단어 수
for idx, i in enumerate(a):
    if idx == 0: # 첫 번째 알파벳이라면
        count += 1
    elif idx == 1:
        count += 1
        for tmp in cro_list:
            if (a[idx-1] + i) == tmp:
                count -= 1
    else:
        count +=1
        if (a[idx-2] + a[idx-1] + i) == 'dz=':
            count -= 2
        else:
            for tmp in cro_list:
                if (a[idx-1] + i) == tmp:
                    count -= 1

print(count)