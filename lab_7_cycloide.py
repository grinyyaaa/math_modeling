import numpy as np
import matplotlib.pyplot as plt
a = 1
for t in np.arange(1, 8*np.pi, 0.01):
    x = a(t - np.sin(t))
    y = a(t - np.cos(t))
    plt.plot(x, y)
plt.savefig('fig_1.png')