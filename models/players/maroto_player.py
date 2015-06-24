class MarotoPlayer:
	def __init__(self, color):
		self.color = color

	def play(self, board):
		return self.getBestMove(board.valid_moves(self.color))

	def getBestMove(self, moves):
		import random
		alwaysPlay = [[1,1],[1,8], [8,1], [8,8]]
		goodMoves = []
		for move in moves:
			temp_move = [move.x,move.y]
			if temp_move in alwaysPlay:
				return move
			if move.x != 2 and move.x != 7 and move.y != 2 and move.y != 7:
				goodMoves.append(move)
		if len(goodMoves) > 0:
			return random.choice(goodMoves)
		else:
			return random.choice(moves)

