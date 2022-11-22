import matplotlib.pyplot as plt
import numpy as np
import random as rdm
fig = plt.figure()
ax = fig.gca(projection = '3d')
theta = np.linspace(0, 4 * np.pi)
z = np.linspace(0, 12)
x = np.cos(theta)
y = np.sin(theta)
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
ax.plot(x, y, z, color = 'gray')
deviation = [-0.08, 0.08]
for i in range(70):
    th = rdm.choice(theta)

    ax.plot(np.cos(th) + rdm.choice(deviation), np.sin(th) + rdm.choice(deviation), (12*th)/(4*np.pi) + rdm.choice(deviation), rdm.choice(['go', 'bo']))
plt.show()