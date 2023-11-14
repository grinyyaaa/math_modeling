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

print(x)
print(y)

