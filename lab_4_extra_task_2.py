import numpy as np
def fib(n):
    a = 1
    b = 1
    for i in np.arange(0, n, 1):
        a = a + b
        print(a)

fib(4)