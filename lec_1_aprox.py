import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()

x = [1, 2, 3]
y = [7, 9, 7]

ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(np.pi/2+np.pi/6 , np.pi/2-np.pi/6, 100)
x = 4 + 2*np.cos(t)
y = 5.25 + 2 * np.sin(t)

ax.plot(x, y, '-', lw=2, color='k')

x = [5, 6, 7]
y = [7, 9, 7]

ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(2 * np.pi, np.pi, 100)
x = 4 + 3*np.cos(t)
y = 7 + 5*np.sin(t)

ax.plot(x, y, '-', lw=2, color='k')


t = np.linspace(np.pi/2+np.pi/4, np.pi/2-np.pi/4, 100)
x = 2.75 + np.cos(t)
y = 4.83 + np.sin(t)

ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(3*np.pi/2-np.pi/4, 3*np.pi/2+np.pi/4, 100)
x = 2.75 + np.cos(t)
y = 6.21 + np.sin(t)

ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(3*np.pi/2-np.pi/4, 3*np.pi/2+np.pi/4, 100)
x = 5.3 + np.cos(t)
y = 6.21 + np.sin(t)

ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(np.pi/2+np.pi/4, np.pi/2-np.pi/4, 100)
x = 5.3 + np.cos(t)
y = 4.83 + np.sin(t)

ax.plot(x, y, '-', lw=2, color='k')

x = [4, 3.5, 4.5, 4]
y = [3.8, 4.48, 4.48, 3.8]

ax.plot(x, y, '-', lw=2, color='k')

t = np.linspace(3*np.pi/2-np.pi/4, 3*np.pi/2+np.pi/4, 100)
x = 4 + np.cos(t)
y = 3.85 + np.sin(t)

ax.plot(x, y, '-', lw=2, color='k')

plt.axis('equal')

plt.savefig('fox.png')


