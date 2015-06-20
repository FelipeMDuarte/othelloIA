MAX = 1
MIN = -1

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

	def evaluate(self):
		if not self.leaf :
			self.generateChildren()
			for node in self.children:
				node.evaluate()
				if self.value == None or (self.type == MAX and node.value > self.value) or  (self.type == MIN and node.value < self.value):
					self.value = node.value 
		else :
			self.calculateValue()	
	
	
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

