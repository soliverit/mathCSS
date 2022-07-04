class Connector():
	##
	#
	# parent:	Node from the prevoius layer
	# child:	Node on the layer after parent
	##
	def __init__(self, parent, child):
		self.parent	= parent
		self.child	= child
		self.weight	= 0
		self.bias	= 0
	def __str__(self):
		return self.parent.name + "\t> " + self.child.name