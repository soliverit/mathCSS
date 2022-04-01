from ..css_block import CSSBlock
class Sum(CSSBlock):
	def __init__(self, handle, properties, targetProperty=False, scale=1):
		super().__init__(handle, targetProperty, scale)
		for property in properties:
			self.addProperty(property)
	def toBlockString(self):
		handle			= self.getHandle()
		properties		= []
		propertyHandles	= []
		for idx in range(len(self.properties)):
			propertyHandle = handle + "-property-" + str(idx)
			propertyHandles.append("var(" + propertyHandle + ")")
			properties.append(propertyHandle + ": " + self.getPropertyString(idx))
		output = ";\n".join(properties) + ";\n"
		output += handle + ": calc(" + " + ".join(propertyHandles) + ");"
		return output
			
		
	
