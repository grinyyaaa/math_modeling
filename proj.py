import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import warnings
import matplotlib
warnings.filterwarnings('ignore', category=matplotlib.MatplotlibDeprecationWarning)

def fall(t, vx0, vy0, angle):
    x = vx0*np.cos(angle) * t
    y = (vy0*np.sin(angle)* t - ((10 * t**2)/2))
    if y < -10:
        y = (-20 - vy0*np.sin(angle) * t + ((10 * t**2)/2))
        x = vx0*np.cos(angle) * t
        if y > 10:
            y = (40 + vy0*np.sin(angle) * t - ((10 * t**2)/2))
            x = vx0*np.cos(angle) * t
            if y < -10:
                y = (-60 - vy0*np.sin(angle) * t + ((10 * t**2)/2))
                x = vx0*np.cos(angle) * t
                if y > 10:
                    y = (80 + vy0*np.sin(angle) * t - ((10 * t**2)/2))
                    x = vx0*np.cos(angle) * t
                    if y < -10:
                        y = (-100 - vy0*np.sin(angle) * t + ((10 * t**2)/2))
                        x = vx0*np.cos(angle) * t


    return x, y

def animate(i):
    ball1.set_data(fall(vx0=4, vy0=12, angle=0.523599, t=i))
    ball2.set_data(fall(vx0=1, vy0=15, angle=0.323599, t=i))
    ball3.set_data(fall(vx0=5, vy0=8, angle=0.223599, t=i))
    ball4.set_data(fall(vx0=2, vy0=10, angle=0.423599, t=i))
    ball5.set_data(fall(vx0=5, vy0=26, angle=0.123599, t=i))
    ball6.set_data(fall(vx0=8, vy0=21, angle=0.623599, t=i))
    ball7.set_data(fall(vx0=6, vy0=14, angle=0.723599, t=i))
    ball8.set_data(fall(vx0=7, vy0=17, angle=0.823599, t=i))
    #print(fall(vx0=4, vy0=20, angle=0.523599, t=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plt.grid()
    ball1, = plt.plot([], [], 'o', ms=8, color='black')
    ball2, = plt.plot([], [], 'o', ms=8, color='red')
    ball3, = plt.plot([], [], 'o', ms=8, color='green')
    ball4, = plt.plot([], [], 'o', ms=8, color='yellow')
    ball5, = plt.plot([], [], 'o', ms=8, color='purple')
    ball6, = plt.plot([], [], 'o', ms=8, color='orange')
    ball7, = plt.plot([], [], 'o', ms=8, color='blue')
    ball8, = plt.plot([], [], 'o', ms=8, color='m')

    edge = 10

    ax.set_xlim(0, 35)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, 
                        animate,
                        frames=np.arange(0, 6, 0.01),
                        interval=30
                        )

ani.save('proj.gif')