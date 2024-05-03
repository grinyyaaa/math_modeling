import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

img = plt.imread('horsehead.jpg')

fig, ax = plt.subplots()

ax.imshow(img)

t1 = np.linspace(np.pi,3*np.pi/2, 10)
x1 = 975 + 120 * np.cos(t1)
y1 = 810 + 80 * np.sin(t1)

t2 = np.linspace(np.pi, 2*np.pi, 10)
x2 = 1100 + 24 * np.cos(t2)
y2 = 680 + 1 * np.sin(t2)

x = np.append(x1, x2)
y = np.append(y1, y2)

t3 = np.linspace(np.pi, 2*np.pi, 10)
x3 = 1200 
y3 = 570 

x = np.append(x, x3)
y = np.append(y, y3)

t4 = np.linspace(np.pi, 3*np.pi/2, 10)
x4 = 1240 + 30 * np.cos(t4)
y4 = 550 + 150 * np.sin(t4)

x = np.append(x, x4)
y = np.append(y, y4)

t5 = np.linspace(0.4*np.pi/2, np.pi/2, 10)
x5 = 1050 + 230 * np.cos(t5)
y5 = 315 + 150 * np.sin(t5)

x = np.append(x, x5)
y = np.append(y, y5)

t6 = np.linspace(np.pi, 2.7*np.pi/2, 10)
x6 = 1150 + 100 * np.cos(t6)
y6 = 430 + 40 * np.sin(t6)

x = np.append(x, x6)
y = np.append(y, y6)

t7 = np.linspace(5*np.pi/2, np.pi * 2.08, 10)
x7 = 1115 + 65 * np.cos(t7)
y7 = 325 + 70 * np.sin(t7)

x = np.append(x, x7)
y = np.append(y, y7)

t8 = np.linspace(5*np.pi/2, np.pi * 2.08, 10)
x8 = 1157
y8 = 345 

x = np.append(x, x8)
y = np.append(y, y8)

t9 = np.linspace(np.pi, 3*np.pi/2, 10)
x9 = 1200 
y9 = 290

x = np.append(x, x9)
y = np.append(y, y9)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], 'g')
plt.ylim(1000, 0)
plt.xlim(850, 1500)
plt.savefig('hh_interpol.png')

