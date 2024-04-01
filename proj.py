import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def fall(t, vx0, vy0, angle, wall):
    x = vx0*np.cos(angle) * t
    y = vy0*np.sin(angle) * t * ((10 * t**2)/2)
#   if x == wall or x == 0 :
#        vx0 = -vx0
    return x, y

def animate(i):
    ball.set_data(fall(vx0=1, vy0=0.0002, angle=30, wall=5, t=i))

    ax.set_title("Движение под углом 30 градусов")

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plt.grid()
    ball, = plt.plot([], [], 'o', ms=8, color='black')

    edge = 5

    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig, 
                        animate,
                        frames=100,
                        interval=50
                        )

ani.save('proj.gif')