import numpy as np


def multi(massive):
    mult = 1
    for element in massive:
        mult =  mult * element
    print(mult)


a = [6, 2, 5, 1]
list = np.array(a)
multi(list)


