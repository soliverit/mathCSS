from ..css_block 		import CSSBlock
from ..css_blocks.power	import Power
class QuadraticFormula(CSSBlock):
	def __init__(self, handle, x, angle, gravity, base, targetProperty=False):
		## Super stuff
		super().__init__(handle, targetProperty)
		## Instance stuff
		self.x	= x
		self.addProperty(angle)
		self.addProperty(gravity)
		self.addProperty(base)
	def angleString(self):
		return self.getPropertyString(0)
	def gravityString(self):
		return self.getPropertyString(1)
	def baseString(self):
		return self.getPropertyString(2)
	def xString(self):
		return self.getPropertyString(3)
	def toBlockString(self):
		handle	= self.getHandle()
		output	= ""
		output	+= 
		squareX	= Power(handle + "-x-squared", self.x)
		prod	= Product(handle + "-gx-squared", [squareX.handle, self.angleString()
		
		output	= self.angleString() + "\n"
		output	+= self.gravityString() + "\n"
		return output
			
		
	
