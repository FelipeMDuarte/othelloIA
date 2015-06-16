class NodeMinMax:
	MAX = 1
	MIN = 0
	def __init__(self, type, key, leaf):
		self.children = []
		self.type =  type
		self.value = None
		self.key = key
		self.leaf =  leaf
	def evaluate(self):
		if not self.leaf :
			for node in self.children:
				node.evaluate()
				if self.value == None or (self.type == NodeMinMax.MAX and node.value > self.value) or  (self.type == NodeMinMax.MIN and node.value < self.value):
					self.value = node.value 
		else :
			self.calculateValue()
		print "######",self.key, self.value		
	
	def calculateValue(self):
		self.value = int(self.key)

		
M = NodeMinMax(NodeMinMax.MAX , "17", True)

N = NodeMinMax(NodeMinMax.MAX , "20", True)

E = NodeMinMax(NodeMinMax.MIN, "6", True)
				
F = NodeMinMax(NodeMinMax.MIN , "f", False)
F.children =[M,N]

G = NodeMinMax(NodeMinMax.MIN , "3" , True)

H = NodeMinMax(NodeMinMax.MIN , "20" , True)

I = NodeMinMax(NodeMinMax.MIN , "30", True)

J = NodeMinMax(NodeMinMax.MIN, "35" , True)

K = NodeMinMax(NodeMinMax.MIN , "20", True)

L = NodeMinMax(NodeMinMax.MIN , "40", True)

D = NodeMinMax(NodeMinMax.MAX, "d", False)
D.children = [K,L]

C = NodeMinMax(NodeMinMax.MAX , "c", False)
C.children = [H,I,J]

B = NodeMinMax(NodeMinMax.MAX, "b", False)
B.children = [E,F,G]

A = NodeMinMax(NodeMinMax.MIN, "a", False)
A.children = [B,C,D]

A.evaluate()


