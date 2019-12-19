import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of data
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

""" 
To Display in a Format that's Easier to Read:
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)
"""

# Make a list that contains all info about every earthquake
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts)) 158

# Extract magnitudes and location data
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# print(mags[:10]) [0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
# print(lons[:5]) [-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
# print(lats[:5]) [33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]

# Map the earthquakes
data = [{
    # A Scattergeo chart type allows you to overlay a scatter plot of geographic data on a map
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,
    'marker': {
        # change size of markers depending on magnitude of each earthquake
        # list comprehension generates size for each value
        'size': [5*mag for mag in mags],
        'color': mags,  # values Plotly should use to determine where each marker falls on colorscale
        'colorscale': 'Viridis',  # color scale that ranges from dark blue to bright yellow
        'reversescale': True,  # bright yellow for lowest values and dark blue for most severe
        # make it clear what colors represent
        'colorbar': {'title': 'Magnitude'}
    }
}]

"""
To see the available color scales
from plotly import colors

for key in colors.PLOTLY_SCALES,keys():
    print(key)
"""

my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
