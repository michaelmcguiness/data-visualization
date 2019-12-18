"""
The Python package Plotly to produce interactive visualizations.
Plotly is particularly useful when you're creating visualizations that 
will be displayed in a browser, because the visualizations will scale
automatically to fit the viewer's screen.
Visualizations that Plotly generates are also interactive; when the user
hovers over certain elements on the screen, information about that element
is highlighted.

In this project, we analyze the results of rolling dice.  When you roll one
regular, six-sided die, you havean equal chance of rolling any of hte numbers.
However, when you use two dice, you're more likely to roll certain numbers
rather than others.  We'll try to determine which numbers are most likely
to occur by generating a data set that represents rolling dice.  Then we'll
plot the results of a large number of rolls to determine which results are more 
likely than others.
"""
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling a D6 and a D10 50,000 times',
                   xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

print(frequencies)
