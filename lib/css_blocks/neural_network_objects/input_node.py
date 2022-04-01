from ...css_property	import CSSProperty
from .base_node 		import BaseNode
class InputNode(BaseNode):
	def __init__(self, handle):
		super().__init__(handle)
	def value(self):
		return [self.value]		# The value function always returns an array of CSSProperty / CCSBlock