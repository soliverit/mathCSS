class Graph():
	def __init__(self, handle, series):
		##
		# Instance stuff
		##
		self.handle	= handle
		self.series	= series
		self.height	= 5	# Div height (temp measures for Point divs)
		self.width	= 5
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
			point.addStaticProperty("left: %spx" %(str(self.width * idx + 5)))
			point.addStaticProperty("display: block")
			point.addStaticProperty("position: absolute")
			point.addStaticProperty("margin: 2px")
			point.addStaticProperty("border: 1px solid black")
			point.addStaticProperty("background: %s" %(self.colour))
			
			## The CSS
			self.css	+= str(self.series[idx]) + "\n"
			## The HTML
			self.html	+= self.makeDiv(point.handle, "", "") + "\n"
		self.html	= self.makeDiv(self.handle, self.html, "background:grey;width:%spx;height:%spx" %(str(self.width * len(self.series)), str(self.width * len(self.series))))
		
	def makeDiv(self, id, value, style=""):
		return "<div id='%s' style='%s' >%s</div>" %(id, style, value)
			
			