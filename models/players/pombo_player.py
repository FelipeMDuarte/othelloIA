INFINITY = 9999
from models.players.pomboEval import PomboEval

class PomboPlayer:
	def __init__(self, color):
		self.color = color
		self.minMaxTreeDepth = 5

	def play(self, board):
		minMax = PomboEval(1, None, 1, self.minMaxTreeDepth, board, self.color)
		minMax.evaluate(-INFINITY,INFINITY)
		
		for child in minMax.children:
			if child.value == minMax.value:
				return child.key
		
		return None
