import matplotlib.pyplot as plt
import numpy as np
import time

plt.ion()
plt.show()

for count in range(10, 100, 2):
    x = np.linspace(0, 20, count)
    plt.clf()
    plt.plot(x, np.sin(x))
    plt.draw()
    plt.pause(0.1)

plt.pause(1)
plt.close()