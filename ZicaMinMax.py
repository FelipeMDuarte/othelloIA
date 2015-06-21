import models.players.minmax as minmax
from models.players.minmax import NodeMinMax
from models.board import Board

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

class ZicaMinMax (NodeMinMax):
	def __init__(self, type, key, depth, maxDepth, board, color):
		minmax.NodeMinMax.__init__(self, type, key, depth, maxDepth)
		self.parent =  None
		self.board = board
		self.color = color
		self.enemyColor = 'o' if color == '@' else '@'
	
	def generateChildren(self):
		moveColor = self.color if self.type == minmax.MAX else self.enemyColor
		
		moves = self.board.valid_moves(moveColor)

		for move in moves:
			nextBoard = self.board.get_clone()
			nextBoard.play(move, moveColor)
			child = ZicaMinMax(self.getChildrenType(), move, self.depth + 1, self.maxDepth, nextBoard, self.color)
			self.children.append(child)
	
	def calculateValue(self):
		self.value = 0

		for i in range(1,9):
			for j in range(1,9):
				if self.board.board[i][j] == self.color:
					weight = WEIGHT_MAP[i-1][j-1]
					self.value += WEIGHTS[weight]
				elif self.board.board[i][j] == self.enemyColor:
					weight = WEIGHT_MAP[i-1][j-1]
					self.value -= WEIGHTS[weight]
