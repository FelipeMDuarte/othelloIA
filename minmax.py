MAX = 1
MIN = -1
INFINITY = 9999

class NodeMinMax:
	def __init__(self, type, key, depth, maxDepth):
		self.children = []
		self.type =  type
		self.value = None
		self.key = key
		self.depth = depth
		self.maxDepth = maxDepth
		self.leaf = (depth == maxDepth)

	def getChildrenType(self):
		return -self.type

	def evaluate(self, alpha, beta):
		if not self.leaf :
			self.generateChildren()
			if len(self.children) == 0:
				#No moves left
				self.calculateValue()
				return self.value

			if self.type == MAX :
				self.value = -INFINITY
				for node in self.children :
					self.value = max(self.value,node.evaluate(alpha,beta))
					if self.value >= beta :
						return self.value
					alpha = max(alpha,self.value)
				return self.value
			else:
				self.value = INFINITY
				for node in self.children :
					self.value = min(self.value,node.evaluate(alpha,beta))
					if self.value <= alpha :
						return self.value
					beta = min(beta,self.value)
				return self.value
		else :
			self.calculateValue()
			return self.value	
	
	
	def generateChildren(self):
		for i in range(1,3):
			n = NodeMinMax(self.getChildrenType(), self.key*5 + i, self.depth+1, self.maxDepth)
			self.children.append(n)
	
	def calculateValue(self):
		self.value = self.key

	def printTree(self):
		print "--" * self.depth, self.__str__()
		for n in self.children:
			n.printTree()
	
	def __str__(self):
		return "(" + ("%d"%(self.key)) + ", " + (("%d"%(self.value)) if self.value else "-") + ", " + ("min" if self.type == MIN else "MAX") + ")"

