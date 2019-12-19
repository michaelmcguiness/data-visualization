import csv

import matplotlib.pyplot as plt
from datetime import datetime

filename = 'csv_data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    # assign the reader object to reader
    reader = csv.reader(f)
    # csv module contains a next() function that returns next line in file
    header_row = next(reader)
    # print(header_row): ['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
    # the enumerate() function returns both the index and value of each item

    # get dates and high and low temperatures from this file.
    dates, lows, highs = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        low = int(row[6])
        high = int(row[5])
        dates.append(current_date)
        lows.append(low)
        highs.append(high)

# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red", alpha=0.5)
ax.plot(dates, lows, c="blue", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()  # draws date labels diagonally to prevent overlap
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
