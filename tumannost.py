import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('tumannost.jpg')

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

t3 = np.linspace(np.pi/2, np.pi/7, 10)
x3 = 262 + 25 * np.cos(t3)
y3 = 234.5 + 100 * np.sin(t3)

x = np.append(x, x3)
y = np.append(y, y3)

t4 = np.linspace(np.pi/3, np.pi/8, 10)
x4 = 273.5 + 25 * np.cos(t4)
y4 = 157 + 135 * np.sin(t4)

x = np.append(x, x4)
y = np.append(y, y4)

t5 = np.linspace(np.pi, 3*np.pi/2.1, 10)
x5 = 321.5 + 25 * np.cos(t5)
y5 = 210 + 125 * np.sin(t5)

x = np.append(x, x5)
y = np.append(y, y5)

t6 = np.linspace(np.pi, 3*np.pi/2.5, 10)
x6 = 345 + 25 * np.cos(t6)
y6 = 86 + 4 * np.sin(t6)

x = np.append(x, x6)
y = np.append(y, y6)

t7 = np.linspace(np.pi, 3*np.pi/2.5, 10)
x7 = 390 
y7 = 72 

x = np.append(x, x7)
y = np.append(y, y7)

t8 = np.linspace(3*np.pi/2, 2*np.pi, 10)
x8 = 390 + 50 * np.cos(t8)
y8 = 251.9 + 180 * np.sin(t8) 

x = np.append(x, x8)
y = np.append(y, y8)

t9 = np.linspace(2.7*np.pi/2, 2*np.pi, 100)
x9 = 468.5 + 60 * np.cos(t9)
y9 = 386 + 150 * np.sin(t9) 

x = np.append(x, x9)
y = np.append(y, y9)

t10 = np.linspace(0, np.pi/2, 100)
x10 = 468.5 + 60 * np.cos(t10)
y10 = 386 + 400 * np.sin(t10) 

x = np.append(x, x10)
y = np.append(y, y10)


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
plt.savefig('tumannost_interpol.png')

