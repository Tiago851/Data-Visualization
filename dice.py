#Class for a dice

#Important Modules
from random import randint

class Dice:
	#Class for one dice

	def __init__(self, num_sides = 6):
		#Six-sided dice
		self.num_sides = num_sides

	def roll(self):
		#Return a random number from 1 to 6
		return randint(1, self.num_sides)
