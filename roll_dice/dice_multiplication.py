import pygal
from die import Die


# create 2 dice
die_1 = Die()
die_2 = Die()

# roll dice and generate results
results = []
for roll_num in range(5000):
	result = die_1.roll() * die_2.roll()
	results.append(result)

# count the frequencies
max_results = die_1.num_sides **2
frequencies = []
for num in range(1, max_results+1):
	frequency = results.count(num)
	frequencies.append(frequency)


# plot results as bar chart
hist = pygal.Bar()

hist.title = "Multiplication results of rolling two D6 5000 times."
hist.x_labels = [x for x in range(1, max_results+1)]
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add("D6+D6", frequencies)
hist.render_to_file("multiply_d6.svg")




