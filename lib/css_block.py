class CSSBlock():
	def __init__(self, handle, targetProperty=False):
		self.handle			= handle
		self.targetProperty	= targetProperty
		self.properties 	= []
	def addProperty(self, property):
		self.properties.append(property)
	def getHandle(self):
		return "--" + self.handle
	def getBlockID(self):
		return "#" + self.handle
	##
	# Get either the numeric value or the string alias
	#
	# ID:	property ID - don't breath that!
	##
	def getPropertyString(self, id):
		if isinstance(self.properties[id], str):
			return "var(" + self.properties[id] + ")"
		return  self.properties[id].valueString()
		
	def __str__(self):
		blockString	= self.getBlockID() + "{\n" + self.toBlockString() 
		if self.targetProperty:
			blockString += "\n" + self.targetProperty + ":var(" + self.getHandle() + ");"
		blockString	+= "\n}"
		return blockString
	def toBlockString(self):
		raise self.__name__ + ": toBlockString hasn't been overridden"