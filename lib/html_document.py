class HTMLDocument():
	HEADER	= """<head>
				<link rel="stylesheet" href="./test/style.css" />
				<link rel="stylesheet" href="./test/static_style.css" />
			</head>"""
	def __init__(self):
		self.objects	= []
	def addObject(self, obj):
		self.objects.append(obj)
	def html(self):
		content = "\n".join([ obj.html for obj in self.objects])
		body	= "<body>\n<div id='content'>\n%s\n</div></body>" %(content)
		return "<html>\n%s%s\n</html>" %(self.HEADER, body)
	def css(self):
		return "\n".join([obj.css + "\n" for obj in self.objects])
	def writeHTML(self, path):
		with open(path, "w") as file:
			file.write(self.html())
	def writeCSS(self, path):
		with open(path, "w") as file:
			file.write(self.css())
