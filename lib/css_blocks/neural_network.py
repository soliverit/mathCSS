from ..css_block 							import CSSBlock
from ..css_blocks.soft_plus					import SoftPlus
from .neural_network_objects.input_layer	import InputLayer
from .neural_network_objects.input_node		import InputNode
from .neural_network_objects.hidden_layer	import HiddenLayer
from .neural_network_objects.hidden_node	import HiddenNode
from .neural_network_objects.output_layer	import OutputLayer
from .neural_network_objects.output_node	import OutputNode
from .neural_network_objects.hidden_layer	import HiddenLayer
from .neural_network_objects.hidden_node	import HiddenNode
from .neural_network_objects.connector		import Connector
class NeuralNetwork(CSSBlock):
	def __init__(self, handle, inputNodeLabels, outputNodeLabels, targetProperty=False, scale=1):
		## Super stuff
		super().__init__(handle, targetProperty, scale)
		## Instance stuff
		self.inputLayer		= InputLayer(inputNodeLabels)
		self.hiddenLayers	= []
		self.outputLayer	= OutputLayer(outputNodeLabels)
	def createHiddenLayer(self, nodeCount, activationFunction=SoftPlus):
		baseHandle	= self.getHandle()
		lastLayerID	= len(self.hiddenLayers) - 1
		lastLayer	= self.inputLayer if lastLayerID == -1 else self.hiddenLayers[lastLayerID]
		newLayer	= HiddenLayer([HiddenNode(baseHandle + "-hidden-" + str(lastLayerID) + "-node-" +str(x)) for x in range(nodeCount)])
		for idx in range(nodeCount):
			newLayerNode	= HiddenNode(baseHandle + "-" + str(idx)) 
			for lastLayerNode in lastLayer.nodes:
				connector	= Connector(lastLayerNode, newLayerNode)
				newLayerNode.addConnector(connector)
				lastLayerNode.addConnector(connector)
			newLayer.addNode(newLayerNode)
		self.hiddenLayers.append(newLayer)
	def tuneConnectors(self, connectorStates):
		for stateID in range(len(connectorStates)):
			state	= connectorStates[stateID]
			## Identify the layers
			if state["first"] == -1:
				firstLayer	= self.inputLayer
			else:
				firstLayer	= self.hiddenLayers[state["first"]]
				
			if state["second"] == len(self.hiddenLayers):
				secondLayer	= self.outputLayer
			else:
				secondLayer = self.hiddenLayers[state["second"]]
			## Identify the nodes
			firstNode			= firstLayer.nodes[state["first_node"]]
			secondNode			= secondLayer.nodes[state["second_node"]]
			connector			= firstNode.findConnector(secondNode)
			connector.weight	= state["weight"]
			connector.bias		= state["bias"]
			
		
	##
	# Overridden stuff
	##
	def toBlockString(self):
		output	= ""
		for idx in range(len(self.outputLayer.nodes)):
			outputNode	= self.outputLayer.nodes[idx]
			value		= outputNode.value()
			output		+= str(CSSProperty(self.getHandle() + "-output-node-" + str(idx), "var(" + value + ")")) + "\n"
		return output
			
		
			
		
	
