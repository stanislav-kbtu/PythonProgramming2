import matplotlib.pyplot as plt
import random as rdm
import numpy as np

countries = ["Germany", 'Australia', 'South Korea', 'US', 'UK', 'India']
numbers = [16.5, 2.2, 9.2, 20.1, 24.9, 27.2]
plt.pie(numbers, explode = [0, 0, 0.1, 0, 0, 0], labels = countries)



plt.title("Population Density Index")
plt.show()