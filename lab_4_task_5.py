import numpy as np

def square(a, r=0, z=0, h=0, i=0, j=0):
    ''' 'Круг - 1. Треугольник - 2. Прямоугольник -3'
    '''
    if a == 1:
        s = r**2 * np.pi
        print(s)
    else:
        print()
    if a == 2:
        s = 0.5 * z * h
        print(s)
    else: 
        print()
    if a == 3:
        s = i * j
        print(s)
    else:
        print()

square(3, i=5, j=6)
