import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import shapely.geometry as geom

#plt.arrow(0, 0, 4, 4, width = 0.02)

x,y = np.meshgrid(np.linspace(-5,5,10), np.linspace(-5,5,10))
u = 1
v = -1
plt.quiver(x,y,u,v)
plt.title('Vector speedo field, V = {1, -1}, m/s ')
plt.xlabel('Coord X, m')
plt.ylabel('Coord Y, m')
plt.savefig('dich3.png')
plt.close()


u = x/np.sqrt(x**2 + y **2)
v = y/np.sqrt(x**2 + y **2)
plt.quiver(x,y,u,v)
plt.title('Vector speedo field, V = {1, -1}, m/s ')
plt.xlabel('Coord X, m')
plt.ylabel('Coord Y, m')
plt.savefig('dich4.png')
plt.close()

u = -y/np.sqrt(x**2 + y**2)
v = x/np.sqrt(x**2 + y**2)
plt.quiver(x,y,u,v)
plt.title('Vector speedo field, V = {1, -1}, m/s ')
plt.xlabel('Coord X, m')
plt.ylabel('Coord Y, m')
plt.savefig('dich5.png')
plt.close()

u = -y/np.sqrt(x**2 + y**2) + y
v = x/np.sqrt(x**2 + y**2)
plt.quiver(x,y,u,v)
plt.title('Vector speedo field, V = {1, -1}, m/s ')
plt.xlabel('Coord X, m')
plt.ylabel('Coord Y, m')
plt.savefig('dich6.png')
plt.close()

