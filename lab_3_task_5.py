import numpy as np

N = 3
M = 5


a = np.zeros((N, M))

for i in np.arange(0, N, 1):
    for j in np.arange(0, M, 1):
        arg = np.sin(N * i + M * j + 1)
        if arg < 0:
            a[i,j] = 0
        else:
            a[i,j] = arg
        slice = a[i,::-1]
    print(slice)
print()
print(a)
        
