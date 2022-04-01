from ..soft_plus	import SoftPlus
class BaseNode():
	def __init__(self, handle, activationFunction=SoftPlus):
		self.handle				= handle
		self.activationFunction	= activationFunction
		self.connectors = []
	def addConnector(self, connector):
		self.connectors.append(connector)
	def getParentConnectors(self):
		parents	= []
		for connector in self.connectors:
			if connector.child == self:
				parents.append(connector)
		return parents
	def getChildConnectors(self):
		children	= []
		for connector in self.connectors:
			if connector.parent == self:
				children.append(connector)
		return children
	def findConnector(self, otherNode):
		for connector in self.connectors:
			if connector.child == otherNode:
				return connector
	def value(self):
		parents	= self.getParentConnectors()
		valueSeries	= []
		for idx in range(len(parents)):
			parent					= parents[idx]
			connectorValueSeries	= parent.value()	##[]CSSProperty
			for cssElement in connectorValueSeries:
				valueSeries.append(cssElement)
			activationFunction	= self.activationFunction(handle + "-" + self.__name__ + "-" + str(idx), connectorValueSeries[-1])
			valueSeries.append(activationFunction)
		return valueSeries