#Visualizing the results from dice rolling

#Important modules
from dice import Dice
from plotly.graph_objs import Bar, Layout
from plotly import offline 

#Creating 
dice_1 = Dice(8) #here it is possible to define how many sides the dice have
dice_2 = Dice(8)

results = []

#Rounds
n = 1000

#Make rolls 
for roll_num in range(n):
	result = dice_1.roll() + dice_2.roll()
	results.append(result)

#Analye the results
frequencies = []

max_result = dice_1.num_sides + dice_2.num_sides

for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

#Visualize the results
x_values = list(range(2, max_result+1))
data = [Bar(x= x_values, y = frequencies)]

x_axis_config = {"title": 'Result', "dtick": 1}
y_axis_config = {"title": "Frequency of results"}

my_layout = Layout(title = f"Rolling two D6 dices {n} times", xaxis = x_axis_config,
	yaxis = y_axis_config)

offline.plot({"data": data, "layout": my_layout}, filename = "d6x2.html")