class MarotoPlayer:
	def __init__(self, color):
		self.color = color

	def play(self, board):
		return self.getBestMove(board.valid_moves(self.color))

	def getBestMove(self, moves):
		alwaysPlay = [[1,1],[1,8], [8,1], [8,8]]
		goodMoves = []
		for move in moves:
			temp_move = [move.x,move.y]
			if temp_move in alwaysPlay:
				return move
			if move.x != 2 or move.x != 7 or move.y != 2 or move.y != 7:
				goodMoves.append(move)
		if len(goodMoves) > 0:
			import random
			return random.choice(goodMoves)
		else:
			return random.choice(moves)

