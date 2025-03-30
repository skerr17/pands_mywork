# write a program that plots the function $y=x^2$
# using matplotlib
# Author: Stephen Kerr

# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# define the x and y points
x = np.array(range(1,100))
y = x * x




# turn this into an import module so moved all 
# the code into a code block for testing 
# (only runs when this file is executed directly)
if __name__ == '__main__':
    # plot the x and y points on plot
    plt.plot(x, y)
    # show the plot
    plt.show()
