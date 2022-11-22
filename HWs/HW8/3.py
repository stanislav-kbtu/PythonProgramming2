import matplotlib.pyplot as plt
import random as rdm
import numpy as np
x_values = np.linspace(0, 10)   
sinus = lambda x: (np.sin((np.pi/5) * x))
minsinus = lambda x: -(np.sin((np.pi/5) * x))
leftsinus = lambda x: -(np.sin(((np.pi/5) * x) - np.pi/2))
minleftsinus = lambda x: (np.sin(((np.pi/5) * x) - np.pi/2))
plt.plot(x_values, list(map(sinus, x_values)))
plt.plot(x_values, list(map(minsinus, x_values)), color = 'green')
plt.plot(x_values, list(map(leftsinus, x_values)), color = 'orange')
plt.plot(x_values, list(map(minleftsinus, x_values)), color = 'red')
plt.show()