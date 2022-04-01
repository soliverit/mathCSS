class HTMLDocument():
	HEADER	= """<head>
				<link rel="stylesheet" href="./test/STYLE_ALIAS.css" />
				<link rel="stylesheet" href="./test/static_style.css" />
				<script type="text/javascript" src="http://code.jquery.com/jquery-latest.min.js" ></script>
				<script src="./test/debug.js"></script>
			</head>"""
	def __init__(self, prefix):
		self.prefix		= prefix
		self.objects	= []
	def addObject(self, obj):
		self.objects.append(obj)
	def html(self):
		content = "\n".join([ obj.html for obj in self.objects])
		body	= "<body>\n<div id='content'>\n%s\n</div></body>" %(content)
		return "<html>\n%s%s\n</html>" %(self.HEADER.replace("STYLE_ALIAS", self.prefix + "_style"), body)
	def css(self):
		return "\n".join([obj.css + "\n" for obj in self.objects])
	def writeHTML(self, path):
		with open(path, "w") as file:
			file.write(self.html())
	def writeCSS(self, path):
		with open(path, "w") as file:
			file.write(self.css())
