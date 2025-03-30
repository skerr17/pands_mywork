# this program has a list of counties 
# and their populations are proportional to the size
# of the piece of pie
# Atuhor: Stephen Kerr

# import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt

# make an array of the counties
counties = np.array(['Dublin', 'Cork', 'Limerick', 'Galway', 'Kerry'])

# make an array of the populations
populations = np.array([1000000, 500000, 300000, 200000, 150000])

# make an array of the colours
colours = np.array(['red', 'blue', 'green', 'yellow', 'purple'])

# plot the pie chart
#plt.pie(populations, labels=counties, colors=colours, autopct='%1.1f%%')

# change the pie chart to a bar chart
plt.bar(counties, populations, color=colours)

# show plot
plt.show()
