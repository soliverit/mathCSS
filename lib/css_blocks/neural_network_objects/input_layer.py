from .base_layer 	import BaseLayer	
from .input_node	import InputNode
class InputLayer(BaseLayer):
	def __init__(self, inputNodeLabels):
		super().__init__(inputNodeLabels)
	def createNode(self, label):
		return InputNode(label)