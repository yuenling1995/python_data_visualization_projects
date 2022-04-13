import pygal
from die import Die


# create 2 dice
die_1 = Die()
die_2 = Die(10)

# roll the dice
results = []
for value in range(50000):
	result = die_1.roll() + die_2.roll()
	results.append(result)


# count the results frequencies
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for num in range(2, max_results+1):
	frequency = results.count(num)
	frequencies.append(frequency)


# plot the frequencies as histrogram
hist = pygal.Bar()

hist.title = "Results of rolling D6 and D10 dice 50000 times."
hist.x_labels = [x for x in range(2, max_results+1)]
hist.x_title = "Result"
hist.y_title = "Frequencies"

hist.add("D6+D10", frequencies)
hist.render_to_file('different_dice.svg')



