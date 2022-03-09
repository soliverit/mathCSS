from ..css_block import CSSBlock
class SimpleLinearRegression(CSSBlock):
	def __init__(self, handle, xSet, ySet, targetProperty=False):
		super().__init__(handle, targetProperty)
		for xProperty in xSet:
			self.addXProperty(xProperty)
		self.yProperties	=[]
		for yProperty in ySet:
			self.addYProperty(yProperty)
	def addXProperty(self, property):
		self.properties.append(property)
	def addYProperty(self, property):
		self.yProperties.append(property)
	def getB0Handle(self):
		return "--" + self.handle + "-B0"
	def getB1Handle(self):
		return "--" + self.handle + "-B1"
	def getXPropertyString(self, idx):
		return self.getPropertyString(idx);
	def getYPropertyString(self, id):
		if isinstance(self.yProperties[id], str):
			return "var(" + self.yProperties[id] + ")"
		return  self.yProperties[id].valueString()
	def toBlockString(self):
		handle		= self.getHandle()
		b0Handle	= self.getB0Handle()
		b1Handle	= self.getB1Handle()
		#
		output		= ""
		xHandles	= []
		yHandles	= []
		# Add normal values
		for idx in range(0, len(self.properties)):
			xHandle	= handle + "-x" + str(idx)
			yHandle	= handle + "-y" + str(idx)
			xHandles.append(xHandle)
			yHandles.append(yHandle)
			output += xHandle + ": " + self.getXPropertyString(idx) + "; " + yHandle + ": " + self.getYPropertyString(idx) + ";\n" 
		## Meanvalues
		meanXHandle	= handle + "-mean-x"
		meanYHandle	= handle + "-mean-y"
		output		+= meanXHandle + ": calc((" + " + ".join(["var(" + x  + ")" for x in xHandles]) + ") / " + str(len(xHandles)) + ");\n"
		output		+= meanYHandle + ": calc((" + " + ".join(["var(" + y  + ")" for y in yHandles]) + ") / " + str(len(yHandles)) + ");\n"
		## Error values
		xesValues	= []
		xesHandle	= handle + "-err-s"
		for idx in range(0, len(self.properties)):
			xErrHandle	= handle + "-err-x" + str(idx)
			yErrHandle	= handle + "-err-y" + str(idx)
			output		+= xErrHandle + ": calc( var(" + xErrHandle + ") - var(" + meanXHandle + ");\n"
			output		+= yErrHandle + ": calc( var(" + yErrHandle + ") - var(" + meanYHandle + ");\n"
			xesValues.append("var(" + xErrHandle + ") * var(" + xErrHandle + ")")
		## X Error sum
		output		+= xesHandle + ":" + " + ".join(xesValues) + ";\n"
			
		## Error S 
		b1Handles	= []
		for idx in range(0, len(self.properties)):
			xErrSHandle	= handle + "-err-x-s" + str(idx)
			yErrSHandle	= handle + "-err-y-s" + str(idx)
			b1Handles.append("var(" + xErrSHandle + ")")
			output		+= xErrSHandle + ": calc(var(" + xErrSHandle + ") * var(" + yErrSHandle	 + "));\n"
		## B1
		b1Handle	= handle + "-" + "B1"
		output		+= b1Handle + ": calc((" + " + \n\t".join(b1Handles) + ") / var(" + xesHandle + "));\n"
		## B
		output		+= handle + ": calc(var(" + meanYHandle + ") - var(" + b1Handle + ") * var(" + meanXHandle + "));\n"
		return output
			
		
	
