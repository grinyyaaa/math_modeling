import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('horsehead.jpg')

fig, ax = plt.subplots()

ax.imshow(img)

t1 = np.linspace(np.pi,3*np.pi/2, 10)
x1 = 970 + 120 * np.cos(t1)
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

t10 = np.linspace(np.pi, np.pi/1.9, 10)
x10 = 1371 + 170 * np.cos(t10)
y10 = 290 + 45 * np.sin(t10)

x = np.append(x, x10)
y = np.append(y, y10)

t11 = np.linspace(-np.pi/2, -0.8, 10)
x11 = 1367 + 95 * np.cos(t11)
y11 = 889 + 550 * np.sin(t11)

x = np.append(x, x11)
y = np.append(y, y11)

t12 = np.linspace(0, np.pi/2.5, 10)
x12 = 1340 + 95 * np.cos(t12)
y12 = 535 + 185 * np.sin(t12)

x = np.append(x, x12)
y = np.append(y, y12)

t13 = np.linspace(0, np.pi/2.5, 10)
x13 = 1320 
y13 = 850

x = np.append(x, x13)
y = np.append(y, y13)

t14 = np.linspace(0, np.pi/2.5, 10)
x14 = 1335 
y14 = 1000

x = np.append(x, x14)
y = np.append(y, y14)

t15 = np.linspace(0, np.pi/2.5, 10)
x15 = 800 
y15 = 1000

x = np.append(x, x15)
y = np.append(y, y15)


spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])
    
polygon = geom.Polygon(curve_coords)
points_number_per_side = 500

x_pictures_limits = [800, 1500]
y_pictures_limits = [0, 1000]

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            plt.plot(x_point_coord, y_point_coord, 'bo', ms = 0.5)

plt.plot(spline_curve[0], spline_curve[1], 'y')
plt.ylim(1000, 0)
plt.xlim(850, 1500)
plt.savefig('hh_interpol.png')

