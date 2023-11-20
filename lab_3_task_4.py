import numpy as np

nxm = np.array([1, 3, 9, 12])

first = np.array([nxm, nxm * 2])
print(first)

slice = nxm[1,0:2:1]
print(slice)