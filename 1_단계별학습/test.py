import numpy as np

if __name__ == "__main__":
    # a = np.full((3, 3), 0)
    # b = np.full((3, 3) ,1)
    # c = np.append(a, b, axis=1)
    # print(c)
    
    x = np.full((1, 1), 1)
    # x[1][1] = 0
    
    one = np.append(x, x, axis=1)
    one = np.append(one, x, axis=1)
    
    tmp = np.full(x.shape, 0)
    two = np.append(x, tmp, axis=1)
    two = np.append(two, x, axis=1)
    
    result = np.append(one, two, axis=0)
    result = np.append(result, one, axis=0)
    
    # print(result)
    
    a = np.array(range(8)).reshape(2, 4)
    for i in a:
        tmp = ''
        for k in i:
            tmp += str(k)
        print(tmp)