import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]  # (list comprehension)

plt.style.use('seaborn')
fig, ax = plt.subplots()

# to change the color of the points, pass c to scatter (c='red')
# (can also use RGB color model: c=(0, 0.8, 0))
# You can alsue use a colorma to emphasize a pattern in the data (see below)
# use s argument to set size of dots
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1_100_000])

plt.show()

"""Saving Your Plots Automatically"""
# If you want your program to automatically save the plot to a file,
# you can replace the call to plt.show() with a call to plt.savefig()

# plt.savefig('squares_plot.png', bbox_inches='tight')
# the second argument trims extra whitespace from the plot. If you want
# extra whitespace around the plot, just omit this argument
