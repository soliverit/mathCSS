class Connector():
	def __init__(self, parent, child):
		self.parent	= parent
		self.child	= child
		self.weight	= 0
		self.bias	= 0