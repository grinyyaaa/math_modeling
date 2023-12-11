import numpy as np

def square(a=0, r=0, z=0, h=0, i=0, j=0):
#'''    Введите 1, если вам нужен круг. Введите 2, если вам нужен треугольник. Введите 3, если вам нужен прямоугольник.'''
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


square(a=3, r=0, z=0, h=0, i=5, j=5)
