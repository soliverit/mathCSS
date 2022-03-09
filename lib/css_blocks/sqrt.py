from ..css_block import CSSBlock
class Sqrt(CSSBlock):
	def __init__(self, handle, property, targetProperty=False):
		super().__init__(handle, targetProperty)
		self.addProperty(property)
	def toBlockString(self):
		handle			= self.getHandle()
		numberHandle	= handle + "-number"
		output			= numberHandle + ": " + self.getPropertyString(0) + ";\n"
		output			+= handle + "-0: calc((var(" + numberHandle + ") + ( var(" + numberHandle + ") / var(" + numberHandle + "))) / 2);\n"
		for idx in range(1, 9):
			propertyHandle	= handle + "-" + str(idx)
			previousHandle	= handle + "-" + str(idx - 1)
			output			+= propertyHandle + ": calc(var(" + previousHandle + ") + " 
			output			+= "( var(" + numberHandle + ") / var(" + previousHandle + ")) / 2);\n"
		return output + handle + ": var(" + handle + "-9);\n"
			
		
	
