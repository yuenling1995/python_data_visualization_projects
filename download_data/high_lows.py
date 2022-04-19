import csv
from matplotlib import pyplot as plt
from datetime import datetime
import temp_functions as tf



sitka_weather = 'sitka_weather_2014.csv'
dv_weather = 'death_valley_2014.csv'

sitka_dates, sitka_highs, sitka_lows = tf.read_file(sitka_weather)
dv_dates, dv_highs, dv_lows = tf.read_file(dv_weather)


# plot data for both datasets
fig = plt.figure(dpi=128, figsize=(10,6))

plt.plot(sitka_dates, sitka_highs, c='red', alpha=0.5)
plt.plot(sitka_dates, sitka_lows, c='blue', alpha=0.5)
plt.fill_between(sitka_dates, sitka_highs, sitka_lows, facecolor='blue', alpha=0.1)

plt.plot(dv_dates, dv_highs, c='green', alpha=0.5)
plt.plot(dv_dates, dv_lows, c='yellow', alpha=0.5)
plt.fill_between(dv_dates, dv_highs, dv_lows, facecolor='pink', alpha=0.3)


# format plot.
title = "Daily high and low temperatures of DV and Sitka - 2014"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()

plt.ylabel("Temperature (F)", fontsize=16)
plt.ylim(0, 120)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()



