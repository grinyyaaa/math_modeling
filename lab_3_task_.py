import numpy as np 
n = 2
m = 4
for i in np.arange(0, m, 1):
    print(i)
for j in np.arange(0, n, 1):
    print(j)

a = np.sin(n * j + m * i)
mxn = np.zeros((m, n))
print(mxn)
mxn[i,j]= a[]