from ..css_block 	import CSSBlock
from ..css_property	import CSSProperty
##
# NOTE: Power must be a CSSProperty
#
#	Uses addProperty for using getPropertyString for the value
##
class Power(CSSBlock):
	def __init__(self, handle, value, power, targetProperty=False):
		super().__init__(handle, targetProperty)
		self.addProperty(value)
		self.power	= power.value if isinstance(power, CSSProperty) else power
	def valueString(self):
		return self.getPropertyString(0)
	def toBlockString(self):
		handle	= self.getHandle()
		outputs	= []
		for idx in range(0, self.power):
			outputs.append(self.valueString())
		return handle + ": calc(" + " * ".join(outputs) + ");"
			
		
	
