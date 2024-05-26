import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('NGC_2264.jpg')

fig, ax = plt.subplots()

ax.imshow(img)

t1 = np.linspace(np.pi, 3*np.pi/2, 10)
x1 = 400 + 50 * np.cos(t1)
y1 = 1200 + 230 * np.sin(t1)

t2 = np.linspace(np.pi/2, 0, 10)
x2 = 410 + 100 * np.cos(t2)
y2 = 957 + 12 * np.sin(t2)

x = np.append(x1, x2)
y = np.append(y1, y2)

t3 = np.linspace(np.pi/2, np.pi/13, 10)
x3 = 511 + 50 * np.cos(t3)
y3 = 770 + 190 * np.sin(t3)

x = np.append(x, x3)
y = np.append(y, y3)

t4 = np.linspace(np.pi, 3*np.pi/2, 10)
x4 = 610 + 50*np.cos(t4)
y4 = 800 + 50*np.sin(t4)

x = np.append(x, x4)
y = np.append(y, y4)

t5 = np.linspace(np.pi/2, 0, 10)
x5 = 610 + 50*np.cos(t5)
y5 = 679 + 70*np.sin(t5)

x = np.append(x, x5)
y = np.append(y, y5)

t6 = np.linspace(np.pi/2, 0, 10)
x6 = 660 + 100*np.cos(t6)
y6 = 630 + 40*np.sin(t6)

x = np.append(x, x6)
y = np.append(y, y6)

t7 = np.linspace(2*np.pi, 3*np.pi/2, 10)
x7 = 701 + 60*np.cos(t7)
y7 = 630 + 230*np.sin(t7)

x = np.append(x, x7)
y = np.append(y, y7)

t8 = np.linspace(np.pi/2, 3*np.pi/2, 10)
x8 = 710 + 20*np.cos(t8)
y8 = 384 + 20*np.sin(t8)

x = np.append(x, x8)
y = np.append(y, y8)

t9 = np.linspace(np.pi/2, np.pi/4, 10)
x9 = 715 + 100*np.cos(t9)
y9 = 313 + 50*np.sin(t9)

x = np.append(x, x9)
y = np.append(y, y9)

t10 = np.linspace(2*np.pi, 3*np.pi/2, 10)
x10 = 715 + 100*np.cos(t10)
y10 = 313 + 120*np.sin(t10)

x = np.append(x, x10)
y = np.append(y, y10)

t11 = np.linspace(np.pi/2, np.pi, 10)
x11 = 715 + 320*np.cos(t11)
y11 = 62 + 130*np.sin(t11)

x = np.append(x, x11)
y = np.append(y, y11)

t12 = np.linspace(0, np.pi/2, 10)
x12 = 250 + 50*np.cos(t12)
y12 = 62 + 315*np.sin(t12)

x = np.append(x, x12)
y = np.append(y, y12)

t13 = np.linspace(3*np.pi/2, np.pi, 10)
x13 = 250 + 200*np.cos(t13)
y13 = 675 + 300*np.sin(t13)

x = np.append(x, x13)
y = np.append(y, y13)

t14 = np.linspace(np.pi, np.pi/2, 10)
x14 = 201 + 150*np.cos(t14)
y14 = 680 + 60*np.sin(t14)

x = np.append(x, x14)
y = np.append(y, y14)

t15 = np.linspace(0, np.pi/2, 10)
x15 = 110 + 120*np.cos(t15)
y15 = 740 + 130*np.sin(t15)

x = np.append(x, x15)
y = np.append(y, y15)

t16 = np.linspace(np.pi, np.pi/2, 10)
x16 = 200 + 120*np.cos(t16)
y16 = 900 + 350*np.sin(t16)

x = np.append(x, x16)
y = np.append(y, y16)

ti = np.linspace(0, 2*np.pi, 10)
xi = 610 + 50 * np.cos(ti)
yi = 560 + 50 * np.sin(ti)

tj = np.linspace(0, 2*np.pi, 10)
xj = 180 + 75 * np.cos(tj)
yj = 620 + 50 * np.sin(tj)



spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])
    
polygon = geom.Polygon(curve_coords)
points_number_per_side = 50

spline_coords, figure_spline_part = interpolate.splprep([xi, yi], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])
    
polygoni = geom.Polygon(curve_coords)
points_number_per_side = 50

spline_coords, figure_spline_part = interpolate.splprep([xj, yj], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])
    
polygonj = geom.Polygon(curve_coords)
points_number_per_side = 100

x_pictures_limits = [0, 800]
y_pictures_limits = [0, 1200]

points_coords = []

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygonj):
            continue
        if p.within(polygoni):
            continue
        if p.within(polygon):
            plt.plot(x_point_coord, y_point_coord, 'bo', ms = 0.5)
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_func = intensity * np.exp(- dec_rate[0]*x**2 - dec_rate[1]*y**2) 
    return scalar_func

intensity_centerums_x = [300, 350, 390, 430, 280, 430, 350, 530, 530, 260, 250, 250, 210, 240, 340, 370, 450, 520, 610, 730, 610, 520, 400, 650]
intensity_centerums_y = [940, 880, 860, 780, 780, 680, 715, 750, 900, 1000, 1200, 1100, 500, 430, 410, 330, 370, 370, 350, 320, 490, 200, 180, 200]
intensity_values = [0.7, 0.9, 2.5, 3, 1, 0.5, 1, 1, 0.5, 0.5, 0.6, 0.7, 0.6, 0.65, 1.3, 1.7, 3, 1.7, 3, 2, 2, 3, 2, 2]

def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
    scalar_field = 0
    for i in range(0, len(int_cen_x)):
        scalar_field += int_vel[i] * bell_function(x-int_cen_x[i], y-int_cen_y[i], 0.005, [0.00025, 0.00025])
    return scalar_field

scalar_fields = []
for i in range(0, len(x_p)):
    calculate = scalar_function(x_p[i], y_p[i], intensity_centerums_x, intensity_centerums_y, intensity_values)
    scalar_fields.append(calculate)

fig, ax = plt.subplots()

sc_plot = ax.scatter(x_p, y_p, c=scalar_fields)
ax.set_ylabel('Координата Y, м')
ax.set_xlabel('Координата X, м')

# ax.imshow(img)
cbar = fig.colorbar(sc_plot)
cbar.set_label("Комбинированное скалярное поле")       

x,y = np.meshgrid(np.linspace(370, 420, 3), np.linspace(780,830,3))
u = -2
v = 2
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(350, 400, 3), np.linspace(710,750,2))
u = 0.2
v = 1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(300, 450, 4), np.linspace(850,870,2))
u = 2
v = 1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(460, 520, 3), np.linspace(720,800,3))
u = -2
v = 0
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(250, 330, 3), np.linspace(900,930,3))
u = -y/np.sqrt(x**2 + y**2) + y
v = x/np.sqrt(x**2 + y**2)
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(330, 520, 5), np.linspace(380,450,3))
u = -1
v = 1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(330, 620, 7), np.linspace(310,350,2))
u = 0
v = 1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(330, 620, 7), np.linspace(230,260,2))
u = -1
v = 0
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(330, 500, 5), np.linspace(179,210,2))
u = -1
v = 0.25
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(570, 630, 4), np.linspace(450,510,3))
u = -1
v = 1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(180,250, 3), np.linspace(450,510,3))
u = -1
v = -1
plt.quiver(x,y,u,v)



plt.title('9')
plt.ylim(1200, 0)
plt.xlim(0, 800)
plt.savefig('NGC_2264.png')


