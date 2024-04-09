import matplotlib.pyplot as plt
import numpy as np

img = plt.imread('horsehead.jpg')

fig, ax = plt.subplots()

ax.imshow(img)


plt.ylim(1000, 0)
plt.xlim(1000, 1500)
plt.savefig('star.png')
