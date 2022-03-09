from ..css_block 	import CSSBlock
from .power			import Power
from .sum			import Sum
from .sqrt			import Sqrt
class Distance(CSSBlock):
	def __init__(self, handle, a, b, targetProperty=False):
		super().__init__(handle, targetProperty)
		self.addProperty(a)
		self.addProperty(b)
	def toBlockString(self):
		handle		= self.getHandle()
		baseHandleA	= handle + "-a"
		baseHandleB	= handle + "-b"
		baseHandleC	= handle + "-c"
		sumHandleC	= handle + "-sum-c"
		sqrtHandle	= handle + "-sqrt"
		aSquared	= Power(baseHandleA, self.properties[0], 2)
		bSquared	= Power(baseHandleB, self.properties[1], 2)
		cSquared	= Sum(sumHandleC, [baseHandleA, baseHandleB])
		distance	= Sqrt(sqrtHandle, sumHandleC)
		output		= "".join([aSquared.toBlockString(), bSquared.toBlockString(), cSquared.toBlockString()]) + ";\n"
		
		return output + "\n" + handle + ":" + distance.getHandle()
	
