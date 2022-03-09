class Graph():
	def __init__(self, handle, serieses):	# serieseseseseseseses
		##
		# Instance stuff
		##
		self.handle		= handle
		self.serieses	= serieses
		self.height		= 5	# Div height (temp measures for Point divs)
		self.width		= 5
		self.colour		= "green"
		self.update()	
	def update(self):
		##
		# Generate data
		##
		self.html	= ""
		self.css	= ""
		for series in self.serieses:
			for idx in range(len(series.values)):
				point		= series.values[idx]
				point.addStaticProperty("height: %spx" %(str(self.height)))
				point.addStaticProperty("width: %spx" %(str(self.width)))
				point.addStaticProperty("left: %spx" %(str(self.width * idx + 5)))
				point.addStaticProperty("display: block")
				point.addStaticProperty("position: absolute")
				point.addStaticProperty("margin: 2px")
				point.addStaticProperty("border: 1px solid black")
				point.addStaticProperty("background: %s" %(series.colour))
				
				## The CSS
				self.css	+= str(series.values[idx]) + "\n"
				## The HTML
				self.html	+= self.makeDiv(point.handle, "", "") + "\n"
		self.html	= self.makeDiv(self.handle, self.html, "background:grey;width:500px;height:350px;" )
		
	def makeDiv(self, id, value, style=""):
		return "<div id='%s' style='position:absolute;%s' >%s</div>" %(id, style, value)
			
			