import numpy as np

a = [7, 1, 4, 9]
list = np.array(a)

def multi(massive):
    first = 1
    for i in np.arange(0, len(a), 1):
        first = first * massive[i]
        print(first)
    

multi(list)
