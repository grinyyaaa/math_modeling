import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('horsehead.jpg')

fig, ax = plt.subplots()

ax.imshow(img)

t = np.linspace(np.pi/2, np.pi/4, 100)
x = 1000 + 100*np.cos(t)
y = 620 + 100*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

x = [1075, 1115]
y = [685, 685]

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(2.3*np.pi/2, 2.7* np.pi/2, 100)
x = 1205 + 100*np.cos(t)
y = 730 + 100*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

plt.ylim(1000, 0)
plt.xlim(850, 1500)
plt.savefig('star.png')


