import numpy as np
def step(a, n):
    b = a
    for u in np.arange(0, n, 1):
        a = a * b
        print(a)

step(2, 10)
