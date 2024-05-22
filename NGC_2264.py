import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('NGC_2264.jpg')

fig, ax = plt.subplots()

ax.imshow(img)

t1 = np.linspace(np.pi, 3*np.pi/2.3, 10)
x1 = 280 + 50 * np.cos(t1)
y1 = 490 + 180 * np.sin(t1)

t2 = np.linspace(np.pi, 3*np.pi/2.65, 10)
x2 = 352 + 100 * np.cos(t2)
y2 = 340 + 12 * np.sin(t2)

x = np.append(x1, x2)
y = np.append(y1, y2)

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])
    
polygon = geom.Polygon(curve_coords)
points_number_per_side = 400

x_pictures_limits = [200, 600]
y_pictures_limits = [0, 700]

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            plt.plot(x_point_coord, y_point_coord, 'bo', ms = 0.5)

plt.plot(spline_curve[0], spline_curve[1], 'r')
plt.ylim(490, 0)
plt.xlim(50, 700)
plt.savefig('NGC_2264.png')