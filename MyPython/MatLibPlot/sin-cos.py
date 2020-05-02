import numpy as np  
import matplotlib.pyplot as plt  
from math import *

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position(('data', 0.0))
ax.spines['bottom'].set_position(('data', 0.0))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

x = np.arange(-100.0, 100.0 , 0.1)  
y = np.sin(x)
plt.plot(x, y)  
y = np.cos(x)
plt.plot(x, y)  
plt.show()  
