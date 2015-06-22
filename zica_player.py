INFINITY = 9999
from models.players.ZicaMinMax import ZicaMinMax

class ZicaPlayer:
	def __init__(self, color):
		self.color = color
		self.minMaxTreeDepth = 3

	def play(self, board):
		minMax = ZicaMinMax(1, None, 1, self.minMaxTreeDepth, board, self.color)
		minMax.evaluate(-INFINITY,INFINITY)
		
		for child in minMax.children:
			if child.value == minMax.value:
				return child.key
		
		return None
