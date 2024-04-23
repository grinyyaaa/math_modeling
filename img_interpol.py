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
x2 = 1000 + 2 * np.cos(t2)
y2 = 800 + 2 * np.sin(t2)

x = np.append(x1, x2)
y = np.append(y1, y2)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

plt.plot(spline_curve[0], spline_curve[1], 'g')
plt.ylim(1000, 0)
plt.xlim(850, 1500)
plt.savefig('hh_interpol.png')

