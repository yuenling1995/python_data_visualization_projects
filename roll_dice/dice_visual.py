import pygal
from die import Die


# create two D6 dice.
die_1 = Die()
die_2 = Die()

# make some rolls, and store results in a list
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# analyze the results
frequencies = []
max_results = die_1.num_sides + die_2.num_sides 

#count the frequencies for the sum of rolling 2 dice
for value in range(2, max_results+1):
	frequency = results.count(value)
	frequencies.append(frequency)

# visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = [x for x in range(2, max_results+1)]
hist.x_title = 'Result'
hist.y_title = "Frequency of Result"

# bar label = D6+D6
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')




