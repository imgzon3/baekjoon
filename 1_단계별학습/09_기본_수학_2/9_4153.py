while True:
    x, y, z = map(int, input().split())
    if x==0 and y==0 and z==0:
        break
    xyz = [x, y, z]
    large = max(xyz)
    xyz.remove(large)
    a = 0
    for i in xyz:
        a += i**2
    if large**2 == a:
        print('right')
    else:
        print('wrong')