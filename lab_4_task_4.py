import numpy as np
a = -4
b = 3

def lightfunc():
    x = np.arange(a, b, 1)
    y = x**2 + 2 
    return y

o = lightfunc()
print(o)

