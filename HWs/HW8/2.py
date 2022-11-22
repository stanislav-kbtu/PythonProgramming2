import matplotlib.pyplot as plt
import random as rdm
import numpy as np

x_values = np.linspace(0.05, 0.55)
px = [rdm.choice(x_values) for i in range(30)]



plt.plot(x_values, x_values, color = 'red')
plt.plot([px[i] + rdm.uniform(-0.02, 0.02) for i in range(30)], [px[i] + rdm.uniform(-0.02, 0.02) for i in range(30)], 'bo')
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Best fit line using regression method")
plt.xlim(0, 0.65)
plt.ylim(0, 0.65)
plt.show()