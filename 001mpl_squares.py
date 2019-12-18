"""
Plots a simple line graph using Matplotlib and then customizes 
it to create a more informative data visualization
"""

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# to use styles, add one line of code before starting to generate the plot:
plt.style.use('seaborn')

# subplots() can generate one or more plots in the same figures
# 'fig' represents the entire figure or collection of plots that are generated
# 'ax' represents a single plot in the figure
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# the plot() method will try to plot the data it's given in a meaningful way

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

# the function plt.show() opens Matplotlib's viewer and displays the plot
plt.show()


""" Using Built-in Styles"""
# Matplotlib has a number of predefined styles available, with good starting
# settings for background colors, gridlines, line widths, fonts, font sizes,
# and more.  To see the styles available on your system, run teh following
# lines in a terminal session:

# >>> import matplotlib.pyplot as plt
# >>> plt.style.available

# ['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight',
# 'seaborn-whitegrid', 'classic', '_classic_test', 'fast', 'seaborn-talk',
# 'seaborn-dark-palette', 'seaborn-bright', 'seaborn-pastel', 'grayscale',
# 'seaborn-notebook', 'ggplot', 'seaborn-colorblind', 'seaborn-muted', 'seaborn',
# 'Solarize_Light2', 'seaborn-paper', 'bmh', 'tableau-colorblind10',
# 'seaborn-white', 'dark_background', 'seaborn-poster', 'seaborn-deep']
