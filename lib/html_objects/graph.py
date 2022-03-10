class Graph():
	def __init__(self, handle, serieses):	# serieseseseseseseses
		##
		# Instance stuff
		##
		self.handle		= handle
		self.title		= handle
		self.serieses	= serieses
		self.height		= 5	# Div height (temp measures for Point divs)
		self.width		= 5
		self.offset		= 0
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
				point.addStaticProperty("left: %spx" %(str(series.scale * idx + 5 + self.offset)))
				point.addStaticProperty("display: block")
				point.addStaticProperty("position: absolute")
				point.addStaticProperty("margin: 2px")
				point.addStaticProperty("border: 1px solid black")
				point.addStaticProperty("z-index: 10")
				point.addStaticProperty("background: %s" %(series.colour))
				
				## The CSS
				self.css	+= str(series.values[idx]) + "\n"
				## The HTML
				self.html	+= self.makeDiv(point.handle, "", "") + "\n"
				
		self.html	= self.makeDiv(self.handle + "-background", self.html, "background:white;top:20px;left:20px;width:460px;height:390px;")
		self.html	+= self.makeDiv(self.handle, self.title, "position:relative !important;border:1px solid;border-collapse:collapse;background:beige;top:30px;left:30px;width:100px;height:20px;")
		self.html	= self.makeDiv(self.handle, self.html, "background:grey;width:500px;height:450px;" )
		
	def makeDiv(self, id, value, style=""):
		return "<div id='%s' style='position:absolute;%s' >%s</div>" %(id, style, value)
			
			