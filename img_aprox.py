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

t = np.linspace(2.3*np.pi/2, 2.9* np.pi/2, 100)
x = 1210 + 100*np.cos(t)
y = 750 + 150*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

x = [1200, 1200]
y = [600, 550]

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(2.3*np.pi/2, 2.65* np.pi/2, 100)
x = 1290 + 100*np.cos(t)
y = 730 + 400*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(np.pi/8, 1.25*np.pi/2, 100)
x = 1110 + 140*np.cos(t)
y = 340 + 120*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(np.pi, 2.5*np.pi/2, 100)
x = 1190 + 140*np.cos(t)
y = 448 + 70*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

x = [1097, 1135]
y = [395, 395]

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(np.pi/5.2, 0.7*np.pi/2, 100)
x = 1078 + 140*np.cos(t)
y = 235 + 180*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

x = [1170, 1190]
y = [336, 336]

ax.plot(x, y, '-', lw=2, color='b')

x = [1170, 1203]
y = [336, 290]

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(np.pi/2, np.pi/1.15, 100)
x = 1335 + 140*np.cos(t)
y = 270 + 65*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(3*np.pi/2, 2*np.pi/1.15, 100)
x = 1330 + 150*np.cos(t)
y = 735 + 400*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(0, np.pi/4, 100)
x = 1283 + 150*np.cos(t)
y = 450 + 360*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

x = [1363, 1385]
y = [730, 710]

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(np.pi, 3*np.pi/2.4, 100)
x = 1465 + 150*np.cos(t)
y = 940 + 290*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(np.pi/2.65, np.pi/1.9, 100)
x = 945 + 150*np.cos(t)
y = 450 + 290*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')

t = np.linspace(np.pi/4.6, np.pi/2.3, 100)
x = 815 + 150*np.cos(t)
y = 550 + 300*np.sin(t)

ax.plot(x, y, '-', lw=2, color='b')



plt.ylim(1000, 0)
plt.xlim(850, 1500)
plt.savefig('star.png')


