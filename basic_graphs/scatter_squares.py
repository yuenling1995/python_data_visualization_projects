import matplotlib.pyplot as plt 

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

#plt.scatter(x_values, y_values, c=(0, 0.5, 0.9), edgecolor='none', s=40)

#plot a color gradient map
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# set chart title and label axes.
plt.title("Square Numbers", fontsize=20)
plt.xlabel("Value", fontsize=10)
plt.ylabel("Square of Value", fontsize=10)

# set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=10)

# set the range for each axis
plt.axis([0, 1100, 0, 1100000])

#plt.show()

# save the figure to a file instead of show it on a screen
plt.savefig('squares_plot.png', bbox_inches='tight')
