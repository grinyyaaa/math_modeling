import numpy as np
def fib(n):
    a = 1
    b = 0
    for fibonacci in range(0, n, 1):
        c = a + b
        a = b
        b = c
        print(c)

fib(8)