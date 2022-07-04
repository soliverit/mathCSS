from ..soft_plus		import SoftPlus
from ...css_property	import CSSProperty
class BaseNode():
	SHOE = 0
	def __init__(self, handle, activationFunction=SoftPlus):
		self.handle				= str(self.__class__.__name__).lower() + "-" + str(self.__class__.SHOE)
		self.activationFunction	= activationFunction
		self.connectors 		= []
		self.name				= str(self.__class__.__name__) + ": " + str(self.__class__.SHOE)
		self.__class__.SHOE	+= 1
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
			if connector.parent == otherNode:
				pass	# Temp: Can't remeber what was going here. Just back after months
	def value(self,f=1):
		parents	= self.getParentConnectors()
		valueSeries	= []
		for idx in range(len(parents)):
			activationHandle		= self.handle + "-node-value-" + str(idx)
			parent					= parents[idx]
			connectorValueSeries	= parent.parent.value()	##[]CSSProperty
			for cssElement in connectorValueSeries:
				valueSeries.append(cssElement)
			print(connectorValueSeries[-1](1))
			exit()
			activationFunction	= self.activationFunction(
				activationHandle + "-" + self.__class__.__name__ + "-" + str(idx), # Dirty!
				connectorValueSeries[-1]
			)

			valueSeries.append(activationFunction)
		return valueSeries
	def __str__(self):
		return self.__class__.__name__ + ": " + self.name 