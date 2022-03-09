##
# Trig credit: https://gist.github.com/stereokai/7666bfe93929b14c2dced148c79e0e97
class CSSProperty():
	def __init__(self, handle, value):
		self.handle		= handle
		self.value		= value
	def valueString(self):
		return str(self.value)
	def getHandle(self):
		return "--" + self.handle
