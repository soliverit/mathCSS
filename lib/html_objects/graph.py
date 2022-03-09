class Graph():
	def __init__(self, handle, series):
		##
		# Instance stuff
		##
		self.handle	= handle
		self.series	= series
		self.height	= 10	# Div height (temp measures for Point divs)
		self.width	= 10
		self.colour	= "green"
		self.update()	
	def update(self):
		##
		# Generate data
		##
		self.html	= ""
		self.css	= ""
		for idx in range(len(self.series)):
			point		= self.series[idx]
			point.addStaticProperty("height: %spx" %(str(self.height)))
			point.addStaticProperty("width: %spx" %(str(self.width)))
			point.addStaticProperty("left: %spx" %(str(self.width * idx)))
			point.addStaticProperty("display: block")
			point.addStaticProperty("position: absolute")
			point.addStaticProperty("background: %s" %(self.colour))
			
			## The CSS
			self.css	+= str(self.series[idx]) + "\n"
			## The HTML
			self.html	+= self.makeDiv(point.handle, "_", "") + "\n"
		self.html	= self.makeDiv(self.handle, self.html, "width%spx" %(str(self.width * len(self.series))))
		
	def makeDiv(self, id, value, style=""):
		return "<div id='%s' style='%s' >%s</div>" %(id, style, value)
			
			