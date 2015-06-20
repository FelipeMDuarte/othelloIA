import minmax

WEIGHT_MAP =   [[6, 7, 8, 9, 9, 8, 7, 6],
		[7, 3, 4, 5, 5, 4, 3, 7],
		[8, 4, 1, 2, 2, 1, 4, 8],
		[9, 5, 2, 0, 0, 2, 5, 9],
		[9, 5, 2, 0, 0, 2, 5, 9],
		[8, 4, 1, 2, 2, 1, 4, 8],
		[7, 3, 4, 5, 5, 4, 3, 7],
		[6, 7, 8, 9, 9, 8, 7, 6]]

WEIGHTS = [3, 15, 3, -40, -5, -5, 120, -20, 20, 5]

def getWeight(pos):
	return WEIGHTS[ WEIGHT_MAP[ pos[0] ][ pos[1] ] ]

class ZicaMinMax :
	def __init__(self, type, key, depth, maxDepth):
		minmax.NodeMinMax.__init__(self, type, key, depth, maxDepth)
		self.parent =  None
	
	def generateChildren(self):
		#TODO
	
	def calculateValue(self):
		#TODO
