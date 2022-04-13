import matplotlib.pyplot as plt 

x_values = list(range(1,6))
y_values = [y**3 for y in x_values]

#plt.scatter(x_values, y_values, c=(0, 0.5, 0.8), s=50)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, edgecolors='none', s=50)

plt.title("Cubes Plot", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of a Number", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
