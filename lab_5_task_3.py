import numpy as np 
import time 

M = 3
N = 6
timer = time.time()
for i in np.arange(M):
    print(i)
    time.sleep(1)
    for j in np.arange(N):
        print(j)
        time.sleep(1) 

print(f'{time.time() - timer}, seconds')

