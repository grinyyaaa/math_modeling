import numpy as np


x0 = 0 
v0 = 10
v0x = np.cos(30) * v0

from lab_3_task_1 import mg_acceleration as maa
 
y0 = 0
v0y = np.sin(30) * v0

t = np.arange(0, 5, 0.01)

x = x0 + v0x * t 
y = y0 + v0y * t - maa * t ** 2 / 2

a = np.zeros((len(x), 3))
for i in np.arange(len(x)):
    a[i,0] = t[i] 
    a[i,1] = x[i]
    a[i,2] = y[i]

print(a)


