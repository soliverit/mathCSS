from ..css_block import CSSBlock
class Product(CSSBlock):
	def __init__(self, handle, properties, targetProperty=False):
		super().__init__(handle, targetProperty)
		for property in properties:
			self.addProperty(property)
	def toBlockString(self):
		handle			= self.getHandle()
		properties		= []
		propertyHandles	= []
		for idx in range(0, len(self.properties)):
			propertyHandle = handle + "-property-" + str(idx)
			propertyHandles.append("var(" + propertyHandle + ")")
			properties.append(propertyHandle + ": " + self.getPropertyString(idx) + ";")
		output = "\n".join(properties) + "\n"
		return	output + handle + ": calc(" + " * ".join(propertyHandles) + ");"
			
		
	
