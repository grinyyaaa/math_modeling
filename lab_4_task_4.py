import numpy as np

def lightfunc(a, b, N):
    x = np.linspace(a, b, N)
    y = x**2 + 2
    return y

a = lightfunc(2, 4, 5)
print(a)