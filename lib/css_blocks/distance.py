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
		baeHnadle	= handle.replace("--", "")
		baseHandleA	= baeHnadle + "-a"
		baseHandleB	= baeHnadle + "-b"
		baseHandleC	= baeHnadle + "-c"
		sumHandleC	= baeHnadle + "-sum-c"
		sqrtHandle	= baeHnadle + "-sqrt"
		##
		# Remove -- so to the double "----"
		##
		aSquared	= Power(baseHandleA, self.properties[0], 2)
		bSquared	= Power(baseHandleB, self.properties[1], 2)
		cSquared	= Sum(sumHandleC, [baseHandleA, baseHandleB])
		distance	= Sqrt(sqrtHandle, sumHandleC)
		output		= ";\n".join([aSquared.toBlockString(), bSquared.toBlockString(), cSquared.toBlockString()]) + "\n"
		output		+= distance.toBlockString() + ";\n"
		return output + "\n" + handle + ": " + distance.getHandle() + ";"
	
