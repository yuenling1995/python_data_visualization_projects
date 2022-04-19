import csv
from matplotlib import pyplot as plt
from datetime import datetime


def read_file(filename):

	with open(filename) as f:
		reader = csv.reader(f)
		header_row = next(reader)

		# print each column name and its index position
		#for index, column_header in enumerate(header_row):
		#	print(index, column_header)

		#  get dates & high, low temperatures from file.
		dates, highs, lows = [], [], []
		for row in reader:
			try:
				current_date = datetime.strptime(row[0], '%Y-%m-%d')
				high = int(row[1])
				low = int(row[3])
			except ValueError:
				print(current_date, 'missing data')
			else:
				dates.append(current_date)
				highs.append(high)
				lows.append(low)

	return dates, highs, lows


















