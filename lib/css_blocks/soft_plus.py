from ..css_block import CSSBlock
class SoftPlus(CSSBlock):
	def __init__(self, handle, x, targetProperty=False, scale=1):
		super().__init__(handle, targetProperty, scale)
		self.addProperty(x)
	def toBlockString(self): 	
		return "%s: log(1 + exp(%s));\n" %(self.getHandle(), self.getPropertyString(0))
		
	
	#softplus(x)=log(1+e^x)