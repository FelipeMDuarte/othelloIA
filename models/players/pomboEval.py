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

class PomboEval (NodeMinMax):
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
			child = PomboEval(self.getChildrenType(), move, self.depth + 1, self.maxDepth, nextBoard, self.color)
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

	
## Ocupacao de canto
		myValue = 0
		oppValue = 0
		if self.board.board[1][1] == self.color :
			myValue+= myValue
		elif self.board.board[1][1] == self.enemyColor :
			oppValue+= oppValue
		if self.board.board[1][8] == self.color:
			myValue+= myValue
		elif self.board.board[1][8] == self.enemyColor:
			oppValue += oppValue
		if self.board.board[8][1] == self.color:
			myValue += myValue
		elif self.board.board[8][1] == self.enemyColor:
			oppValue+= oppValue
		if self.board.board[8][8] == self.color:
			myValue+= myValue
		elif self.board.board[8][8] == self.enemyColor:
			oppValue+=oppValue
		c = 25 * (myValue - oppValue);
			
			## ocupacao perto de canto
			
		myValue =0 
		oppValue=0
		if self.board.board[1][1] == '.' :
			if self.board.board[1][2] == self.color:
				myValue+=myValue
			elif self.board.board[1][2] == self.enemyColor:
				oppValue+=oppValue
			if self.board.board[2][2] == self.color :
				myValue+=myValue
			elif self.board.board[2][2] == self.enemyColor:
				oppValue+= oppValue
			if self.board.board[2][1] == self.color :
				myValue+=myValue
			elif self.board.board[2][1] == self.enemyColor:
				oppValue+=oppValue
			
		if self.board.board[1][8] == '.' :
			if self.board.board[1][7] == self.color:
				myValue+=myValue
			elif self.board.board[1][7] == self.enemyColor:
				oppValue+=oppValue
			if self.board.board[2][7] == self.color:
				myValue+=myValue
			elif self.board.board[2][7] == self.enemyColor:
				oppValue+=oppValue
			if self.board.board[2][8] == self.color:
				myValue+= myValue
			elif self.board.board[2][8] == self.enemyColor:
				oppValue+=oppValue
		
		if self.board.board[8][1] == '.':   
			if self.board.board[8][2] == self.color: 
				myValue+=myValue		
			elif self.board.board[8][2] == self.enemyColor: 
				oppValue+=oppValue
			if self.board.board[7][2] == self.color: 
				myValue+=myValue
			elif self.board.board[7][2] == self.enemyColor: 
				oppValue+=oppValue
			if self.board.board[7][1] == self.color: 
				myValue+=myValue
			elif self.board.board[7][1] == self.enemyColor: 
				oppValue+=oppValue
		
		if self.board.board[8][8] == '.':   
			if self.board.board[7][8] == self.color:
				myValue+=myValue
			elif self.board.board[7][8] == self.enemyColor:
				oppValue+=oppValue
			if self.board.board[7][7] == self.color:
				myValue+=myValue
			elif self.board.board[7][7] == self.enemyColor: 
				oppValue+=oppValue
			if self.board.board[8][7] == self.color:
				myValue+=myValue
			elif self.board.board[8][7] == self.enemyColor:
				oppValue+=oppValue
		
		l = -12.5 * (myValue - oppValue);
		
	## Mobilidade

		myValue = len(self.board.valid_moves(self.color))
		oppValue = len(self.board.valid_moves(self.enemyColor))
		if myValue > oppValue :
			m = (100.0 * myValue)/(myValue + oppValue)
		elif myValue < oppValue :
			m = -(100.0 * oppValue)/(myValue + oppValue)
		else:
			m = 0;
	## Peso final de avaliacao
		self.avaliacao = (8 * c) + (3 * l) + m + (5*self.value)
		self.value = self.avaliacao