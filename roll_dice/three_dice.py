import pygal
from die import Die

# create 3 dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

# roll the dice and generate results
results = []
for roll_num in range(100):
	result = die_1.roll() + die_2.roll() + die_3.roll()
	results.append(result)

# count the frequencies for results
max_results = die_1.num_sides * 3
frequencies = []

for num in range(3, max_results+1):
	frequency = results.count(num)
	frequencies.append(frequency)

# plot frequencies as bar chart
hist = pygal.Bar()

hist.title = "Results of rolling 3 D6 dice 100 times."
hist.x_labels = [x for x in range(3, max_results+1)]
hist.x_title = "Results"
hist.y_title = "Frequency of Results"

hist.add("3 D6", frequencies)
hist.render_to_file("three_dice.svg")



