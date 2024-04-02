import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import warnings
import matplotlib
warnings.filterwarnings('ignore', category=matplotlib.MatplotlibDeprecationWarning)

def fall(t, vx0, vy0, angle):
    x = vx0*np.cos(angle) * t
    y = vy0*np.sin(angle) * t - ((10 * t**2)/2)
    if y < -10:
        y = -17 -vy0*np.sin(angle) * t - ((10 * t**2)/2)

    return x, y

def animate(i):
    ball.set_data(fall(vx0=4, vy0=20, angle=30, t=i))
    print(fall(vx0=4, vy0=20, angle=30, t=i))

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plt.grid()
    ball, = plt.plot([], [], 'o', ms=8, color='black')

    edge = 10

    ax.set_xlim(0, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, 
                        animate,
                        frames=np.arange(0, 5, 0.01),
                        interval=30
                        )

ani.save('proj.gif')