from ..css_block import CSSBlock
class Cos(CSSBlock):
	def __init__(self, hnd, angle, targetProperty=False):
		super().__init__(hnd, targetProperty)
		self.addProperty(angle)
	def toBlockString(self):
		hnd		= self.getHandle()
		aHnd	= hnd + "-deg"
		output	= aHnd + ":" + self.getPropertyString(0) + ";\n"
		output	+= hnd + "-0: 1;\n"
		output	+= hnd + "-1: calc((var(" + aHnd + ") * var(" + aHnd + ")) / 2);\n"
		output	+= hnd + "-2: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 24);\n"
		output	+= hnd + "-3: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 720);\n"
		output	+= hnd + "-4: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 40320);\n"
		output	+= hnd + ": calc(var(" + hnd + "-0" + ") - var(" + hnd + "-1) + var(" + hnd + "-2) - var(" + hnd + "-3) + var(" + hnd +"-4));\n" 
		return output
		
# // Cosine function representation
# .cos {
# --cos1: 1;
# --cos2: calc((var(" + aHnd + ") * var(" + aHnd + ")) / 2);
# --cos3: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 24);
# --cos4: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 720);
# --cos5: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 40320);
# --%s: calc(var(--cos1) - var(--cos2) + var(--cos3) - var(--cos4) + var(--cos5));
# }
