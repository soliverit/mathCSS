from .base_layer	import BaseLayer
from .output_node	import OutputNode
class OutputLayer(BaseLayer):
	def __init__(self, nodeLabels):
		super().__init__(nodeLabels)
	def createNode(self, label):
		return OutputNode(label)