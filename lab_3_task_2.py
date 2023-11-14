import numpy as np

a = 9,8 * 100 * np.tan(30)**2
b = 2 * np.cos(np.pi/3)**2 * (1 - np.tan(30) * np.tan(np.pi/3))

v = np.sqrt(a / b)
print(v)

from lab_3_task_1 import eiler_num as en
from lab_3_task_1 import plank_num as pn
from lab_3_task_1 import bolcman_num as bn

a = 2 * pn * np.e**(-300/bn * 200) * 300**(200/2)
b = np.sqrt(np.pi) * (bn * 200)**(3/2)
n = a / b 
print(n)

