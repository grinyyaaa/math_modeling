import numpy as np

a = [7, 1, 4, 9]
list = np.array(a)

def multi(n):
    k = int(input('введите множитель: '))
    j = n * k 
    print(j)

multi(list)
