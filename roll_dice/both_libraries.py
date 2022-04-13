this file uses both Pygal and Matplotlib to revisit the random_walk and roll_dice exercise




import pygal
import matplotlib.pyplot as plt 
from die import Die
from random_walk import RandomWalk



die = Die()

# roll die and generate results
results = []
for roll_num in range(5000):
	result = die.roll()
	results.append(result)

# count frequencies
frequencies = []
for num in range(1, 7):
	frequency = results.count(num)
	frequencies.append(frequency)

# set screen size
plt.figure(figsize=(10,6))

x_values = list(range(1,7))
plt.title("Results of rolling a die 5000 times")
plt.xlabel("Results", fontsize=10)
plt.ylabel("Frequencies", fontsize=10)

# set size of tick labels
plt.tick_params(axis='both', labelsize=8)


plt.plot(x_values, frequencies, c=(0, 0.5, 0.9), linewidth=3)
plt.show()


#######################################Random Walk####################################################

rw = RandomWalk()
rw.fill_walk()

scatter= pygal.XY(stroke = False)
scatter.title = "Random Walk"

# generate results, create a tuple to store (x,y) and put in list - results
results = []
for i in range(0, len(rw.x_values)):
	result = (rw.x_values[i], rw.y_values[i])
	results.append(result)


scatter.add("walk point", results)
scatter.render_to_file("walk_point.svg")

