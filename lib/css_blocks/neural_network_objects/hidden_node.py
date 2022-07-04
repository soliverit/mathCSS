from .base_node 		import BaseNode
from ...css_property	import CSSProperty
from ..sum				import Sum
class HiddenNode(BaseNode):
	def __init__(self, handle):
		super().__init__(handle)
