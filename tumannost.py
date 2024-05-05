import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('tumannost.jpg')

fig, ax = plt.subplots()

ax.imshow(img)

t1 = np.linspace(- np.pi/2, - np.pi, 10)
x1 = 485
y1 = 100 

t2 = np.linspace(np.pi, np.pi/1.0001, 10)
x2 = 510 + 1 * np.cos(t2)
y2 = 110 + 1 * np.sin(t2)

x = np.append(x1, x2)
y = np.append(y1, y2)

t3 = np.linspace(np.pi, np.pi/1.5, 10)
x3 = 561 + 50 * np.cos(t3)
y3 = 116 + 3 * np.sin(t3)

x = np.append(x, x3)
y = np.append(y, y3)

t4 = np.linspace(np.pi, 2.9*np.pi/2, 10)
x4 = 619 + 84 * np.cos(t4)
y4 = 81 + 5 * np.sin(t4)

x = np.append(x, x4)
y = np.append(y, y4)


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], 'r')
plt.ylim(0, 700)
plt.xlim(50, 950)
plt.savefig('tumannost_interpol.png')

