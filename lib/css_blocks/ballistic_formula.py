from ..css_block 			import CSSBlock
from ..css_blocks.sum		import Sum
from ..css_blocks.power		import Power
from ..css_blocks.product	import Product
class BallisticFormula(CSSBlock):
	def __init__(self, handle, time, gravity, velocity, targetProperty=False):
		## Super stuff
		super().__init__(handle, targetProperty)
		## Instance stuff
		self.addProperty(gravity)
		self.addProperty(velocity)
		self.addProperty(time)
		
	##
	# Getter
	##
	## CSSProperty
	def gravity(self):
		return self.properties[0]
	def velocity(self):
		return self.properties[1]
	def time(self):
		return self.properties[2]
	## Var or numeric string
	def gravityString(self):
		return self.getPropertyString(0)
	def velocityString(self):
		return self.getPropertyString(1)
	def timeString(self):
		return self.getPropertyString(2)
	##
	# Overridden stuff
	##
	def toBlockString(self):
		handle		= self.getHandle()
		##
		# Do math
		##
		output		= ""
		## Add some constants
		gravity		= handle + "-gravity"
		time		= handle + "-time"
		velocity	= handle + "-velocity"
		halfNumber	= handle + "-half-number"
		output		+= halfNumber + ": -0.5;\n"
		output		+= gravity + ": " + str(self.gravity().value) + ";\n"
		output		+= time + ": " + str(self.time().value) + ";\n"
		output		+= velocity + ": " + str(self.velocity().value) + ";\n"
		## Do math
		timeSquared	= Power(self.handle + "-time-squared", time, 2)
		gravityTime	= Product(self.handle + "-y", [halfNumber, gravity, timeSquared.getHandle()])
		velocityTime= Product(self.handle + "-vt", [velocity, time])
		y			= Sum(handle + "-y", [velocityTime.getHandle(), gravityTime.getHandle()])
		## Update outputs
		output 		+= timeSquared.toBlockString() + "\n"
		output 		+= gravityTime.toBlockString() + "\n"
		output 		+= velocityTime.toBlockString() + "\n"
		output 		+= y.toBlockString() + "\n"
		
		
		return output + handle + ": var(" + y.getHandle() + ");\n"
			
		
	
