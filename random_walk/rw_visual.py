import matplotlib.pyplot as plt 
from random_walk import RandomWalk


keep_running = True

# keep making new walks, as long as the program is active:
while keep_running:
	# make a random walk with custom points, and plot the points
	rw = RandomWalk(5000)
	rw.fill_walk()

	# set the size of the plotting window.
	plt.figure(figsize=(10,6))

	# create a colormap, color based on the list of number of points
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Purples, edgecolors='none', s=20)

	# emphasize the first and last points.
	plt.scatter(0, 0, c='green', edgecolors='none', s=100)
	plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

	# remove the axes.
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







