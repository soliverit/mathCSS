from .base_layer	import BaseLayer
from .hidden_node	import HiddenNode
class HiddenLayer(BaseLayer):
	def __init__(self, nodeLabels):
		super().__init__(nodeLabels)
	def createNode(self, label):
		return HiddenNode(label)