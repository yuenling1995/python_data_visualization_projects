import pygal
from die import Die



# create two D8 dice.
die_1 = Die(8)
die_2 = Die(8)

# roll the dice and generate results
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)


# count the frequencies
max_results = die_1.num_sides + die_2.num_sides
frequencies = []

for value in range(2, max_results+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# plot the frequencies as bar chart
hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 1000 times."
hist.x_labels = [x for x in range(2, max_results+1)]
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add("D8+D8", frequencies)
hist.render_to_file("roll_d8_dice.svg")




