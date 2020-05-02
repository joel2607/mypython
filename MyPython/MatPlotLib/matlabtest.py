import matplotlib.pyplot as plt
import numpy as np

x = y = np.arange(-10000.0,10000.0,0.1)

ax = plt.plot(x)

plt.axis([-10,10,-10,10])
plt.show()