import numpy as np
def step():
    a = 2
    n = 4
    for u in np.arange(0, n, 1):
        a = a * a
        print(a) 
step()       
