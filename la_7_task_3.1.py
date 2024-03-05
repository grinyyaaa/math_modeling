from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

xdata, ydata = [], []

def animate(t):
    xdata.append(16*(np.sin(t))**3)
    ydata.append(13*np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t))
    heart.set_data(xdata, ydata)
    return heart,

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plt.axis('equal')
    heart, = plt.plot([], [], '*', color='r', label='Heart')
    edge = 20
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)
    ani = FuncAnimation(fig, 
                        animate,
                        frames=np.arange(0, 2*np.pi, 0.05),
                        interval=30
                        )
    ani.save('Lab_7_task3.1.gif')