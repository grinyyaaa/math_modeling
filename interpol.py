import matplotlib.pyplot as plt
import numpy as np

from scipy import interpolate
t = np.linspace (0, 7, 20)
R = 1
x = R*np.cos(t)
y = R*np.sin(t)

spline_coords, figure_spline_part = interpolate.splprep([x,y], s = 0)

figure_spline_part_manual = np.arange(0, 0.6, 0.01)

spline_curve = interpolate.splev(figure_spline_part_manual, spline_coords)
plt.plot(spline_curve[0], spline_curve[1], color  = 'g')

plt.axis ('equal')
plt.plot(x, y, 'o', color = 'b')
plt.savefig('KILL5.png')