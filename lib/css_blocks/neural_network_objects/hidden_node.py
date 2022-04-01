from .base_node import BaseNode
class HiddenNode(BaseNode):
	def __init__(self, handle):
		super().__init__(handle)
	def value(self):
		values	= []
		for connector in self.connectors():
			parentNode	= connector.parent
			parentValue	= parentNode.value()
			values.append(CSSProperty(parentValue	* conector.weight + connector.bias))