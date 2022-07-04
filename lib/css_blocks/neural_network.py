from ..css_block 							import CSSBlock
from ..css_property							import CSSProperty
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
		self.inputLayer			= InputLayer(inputNodeLabels)
		self.hiddenLayers		= []
		self.outputLayer		= OutputLayer(outputNodeLabels)
		self.outputConnected	= False
	def createHiddenLayer(self, nodeCount, activationFunction=SoftPlus):
		if self.outputConnected:
			print("NeuralNetwork: Ouptut layer connected, can't add hidden layers")
			return
		baseHandle	= self.getHandle()
		lastLayerID	= len(self.hiddenLayers) - 1
		lastLayer	= self.inputLayer if lastLayerID == -1 else self.hiddenLayers[lastLayerID]
		newLayer	= HiddenLayer([HiddenNode(baseHandle + "-hidden-" + str(lastLayerID) + "-node-" +str(x)) for x in range(nodeCount)])
		for node in newLayer.nodes:
			for lastLayerNode in lastLayer.nodes:
				connector	= Connector(lastLayerNode, node)
				node.addConnector(connector)
				lastLayerNode.addConnector(connector)
		self.hiddenLayers.append(newLayer)
	
	def connectOutputLayer(self):	# Could be shared by addHiddenLayer
		for outputNode in self.outputLayer.nodes:
			for hiddenNode in self.hiddenLayers[-1].nodes:
				connector	= Connector(hiddenNode, outputNode)
				hiddenNode.addConnector(connector)
				outputNode.addConnector(connector)
		self.outputConnected	= True
	def tuneConnectors(self, connectorStates):
		if not self.outputConnected:
			self.connectOutputLayer()

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
			
		
	def getConnectors(self):
		connectors	= []
		for layer in [self.inputLayer, self.outputLayer] + self.hiddenLayers:
			for node in layer.nodes:
				for connector in node.connectors:
					if connector not in connectors:
						connectors.append(connector)
		return connectors
	def printConnectors(self):
		for connector in self.getConnectors():
			print(connector)
	##
	# Overridden stuff
	##
	def toBlockString(self):
		output	= ""
		for idx in range(len(self.outputLayer.nodes)):
			outputNode	= self.outputLayer.nodes[idx]
			value		= outputNode.value()
			print(value[-1])
			output		+= str(CSSProperty(self.getHandle() + "-output-node-" + str(idx), "var(" + outputNode.getHandle() + ")")) + "\n"
		return output
	def superCoolPrint(self):
		# Setup
		xSpacing	= 2								# Number of spaces after name
		ySpacing	= 2								# Number of lines per node row
		maxNodes	= 0								# Number of rows before spacing
		maxNodeName	= 0								# Max node name length
		layerCount	= len(self.hiddenLayers) + 2	# Number of layers
		layers		= [self.inputLayer] + self.hiddenLayers + [self.outputLayer]
		for layer in layers:
			maxNodes	= layer.nodeCount() if layer.nodeCount() > maxNodes	else maxNodes
			for node in layer.nodes:
				maxNodeName	= len(node.name) if len(node.name) > maxNodeName else maxNodeName
		nameLength	= maxNodeName + xSpacing
		columnWidth	= nameLength + 3
		lineLength	= layerCount * (maxNodeName + ySpacing)	+ (layerCount - 1)	* 3		# Last bit for spacer |					# Number of characters on each line
		lineArrays	= [ list(" " * lineLength) for i in range(maxNodes * ySpacing)]	# The strings for each line on the console
		lineCount	= len(lineArrays)
		# Draw stuff
		
		for layerID in range(layerCount):
			
			layer		= layers[layerID]
			oddOffset	= 0 if layer.nodeCount() % 2 == 0 else 0
			maxDiff		= maxNodes - layer.nodeCount()
			baseSpacer	= int(float(maxNodes) / layer.nodeCount())
			# Layer dividers
			if layerID + 1 != layerCount:
				position	=layerID * (nameLength + 1) + (nameLength + 1)
				
			xNodePosition	= layerID * nameLength
			# Nodes
			for nodeID in range(layer.nodeCount()):
				node			= layer.nodes[nodeID]
				name			= node.name

				nameChars		= name.split()
				yNodePosition	= (baseSpacer  + ySpacing * nodeID) + oddOffset 	# Which row
				for charID	in range(len(name)):
					lineArrays[yNodePosition][xNodePosition + charID] = name[charID]
		# Print
		for line in lineArrays:
			print("".join(line))
					
			
		
	
