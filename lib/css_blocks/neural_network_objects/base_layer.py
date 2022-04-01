class BaseLayer():
	def __init__(self, nodeLabels):
		self.nodes	= [self.createNode(label) for label in nodeLabels]
	def addNode(self, node):
		self.nodes.append(node)
	def createNode(self, label):
		raise "BaseLayer: createNode isn't overridden with a method returning a NodeType(BaseNode)"