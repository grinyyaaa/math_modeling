import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom
import random 

fig, ax = plt.subplots()

N = 1000

x, y = np.zeros(N), np.zeros(N)
for i in range(N):
    x[i] = random.uniform(0, 1)
    y[i] = random.uniform(0, 1)

scalar_field = 50 * np.sqrt(x**2 + y**2)






sc_plot = ax.scatter(x, y, c=scalar_field)
ax.set_xlabel('Coord x, m')
ax.set_ylabel('Coord y, m')
cbar = fig.colorbar(sc_plot)
cbar.set_label('Scalar field temperature, °C')

plt.savefig('dich.png')







