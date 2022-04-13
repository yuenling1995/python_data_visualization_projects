import matplotlib.pyplot as plt 
from random_walk import RandomWalk


keep_running = True
while keep_running:
	rw = RandomWalk()
	rw.fill_walk()

	# set size of the plotting window.
	plt.figure(figsize=(10, 6))

	plt.plot(rw.x_values, rw.y_values, linewidth=4, c=(0, 0.5, 0.9))

	# emphasize the first and last points.
	#plt.scatter(rw.x_values[0], rw.y_values[0], c='green', edgecolors='none', s=100)
	#plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

	# remove the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)

	plt.show()

	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'y':
		continue
	elif keep_running == 'n':
		break
	else:
		break
