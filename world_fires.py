#Size of the points reduced on purpose to run faster

#Important modules
import csv
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
from datetime import datetime

#Explore the structure of the data
filename = "data/world_fires_7_day.csv"

with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	print(header_row)

	#Extracting fire information
	brightness, lons, lats, daynight, date = [], [], [], [], []

	#Look for the relevant information
	lat_index = header_row.index("latitude")
	lon_index = header_row.index("longitude")
	bright_index = header_row.index("bright_ti4")
	dn_index = header_row.index("daynight")
	day_index = header_row.index("acq_date")

	for row in reader:
		
		try:
			bright = float(row[bright_index])
			lat = float(row[lat_index])
			lon = float(row[lon_index])
			dn = row[dn_index]
			day = datetime.strptime(row[day_index], "%Y-%m-%d")
		except:
			print(f"N/A")
		else:
			lats.append(lat)
			lons.append(lon)
			brightness.append(bright)
			daynight.append(dn)
			date.append(day.date())

data = [{
		'type': 'scattergeo',
		"lon":lons, 
		"lat": lats,
		"text": daynight,
		"marker": {
			"size":[brightn/100 for brightn in brightness],
			"color": [brightn/100 for brightn in brightness],
			"colorscale": "Hot",
			"reversescale": True,
			"colorbar": {"title": "Brightness/100"},
			},
		}]

my_layout = Layout(title= "Global Fires 2018")

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename = "global_fires.html")

f.close()
