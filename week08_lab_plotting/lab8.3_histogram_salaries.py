# program creates a histogram of the salaries
# created in lab8.1_salaries.py using matplotlib
# Author: Stephen Kerr

# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# import lab8.1_salaries
from  lab8_1_sallaries import salaries

# plot the histogram of the salaries
plt.hist(salaries, bins=10, edgecolor='black')

# show the plot
plt.show()