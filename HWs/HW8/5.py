import matplotlib.pyplot as plt
import random as rdm
import numpy as np

countries = ["Germany", 'Australia', 'South Korea', 'US', 'UK', 'India', 'Italy', 'Ireland', 'Belgium', 'Denmark', 'Greece']

numbers = [16.5, 2.2, 9.2, 20.1, 24.9, 27.2, 32.5, 3.2, 17.2, 18.1, 28.9]
plt.pie(numbers, labels = countries, autopct='%1.1f%%', startangle = 45)
plt.legend()
plt.show()