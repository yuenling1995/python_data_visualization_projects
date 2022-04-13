from random import choice


class RandomWalk():
	""" A class to generate random walks."""


	def __init__(self, num_points=50):
		"""initialize attributes of a walk."""
		self.num_points = num_points

		# all walks start at (0, 0)
		self.x_values = [0]
		self.y_values = [0]


	def fill_walk(self):
		""" calculate all the points in the walk."""

		# keep taking steps until the walk reaches the desired length.
		while len(self.x_values) < self.num_points:
			# decide which direction to go and how far to go in that direction
			x_step, y_step = self.get_step()

			# reject moves that go nowhere (from choice)
			if x_step == 0 and y_step == 0:
				continue

			# calculate the next x and y values (last value from the list + steps)
			next_x = self.x_values[-1] + x_step 
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)



	def get_step(self):
		x_direction = choice([1, -1])
		x_distance = choice(list(range(0, 6)))
		x_step = x_direction * x_distance

		y_direction = choice([1, -1])
		y_distance = choice(list(range(0, 6)))
		y_step = y_direction * y_distance

		return x_step, y_step






