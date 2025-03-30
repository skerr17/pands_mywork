# program that plots a scatter plot of ages 
# notes ages between 18 and 65
# imports the salaiers from lab8.1_salaries.py
# using matplotlib
# Author: Stephen Kerr

# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# import salaries
from lab8_1_sallaries import salaries

# create a list of ages random use a seed
np.random.seed(12)
ages = np.random.randint(18, 65, len(salaries))

# plot scatter plot
plt.scatter(ages, salaries, color='red')
# add labels and title
plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.title('Scatter plot of ages and salaries')

# add legend
plt.legend()

# import y = x^2 from lab8_2_plotting.py
from lab8_2_plotting import x, y

# plot the x and y points on plot
plt.plot(x, y, color='blue', label='y=x^2')

# show the plot
plt.savefig('prettier_plot.png')