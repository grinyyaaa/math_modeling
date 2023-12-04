import numpy as np

def lightfunc():
    a = int(input('введите старт промежутка: '))
    b = int(input('введите стоп промежутка: '))
    x = np.arange(a, b, 1)
    y = x**2 + 2 
    return y

o = lightfunc()
print(o)

