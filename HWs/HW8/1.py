import matplotlib.pyplot as plt
import random as rdm
plt.title("This is the Title")
plt.plot([i for i in range(30)], [rdm.randint(1, 100) for i in range(30)], 'b^', linestyle="-", label = 'a')
plt.legend()
plt.xlabel("This is the X Axis")
plt.ylabel("This is the Y Axis")
plt.show()