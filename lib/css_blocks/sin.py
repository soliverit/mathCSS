from ..css_block import CSSBlock		
class Sin(CSSBlock):
	def __init__(self, hnd, angle, targetProperty=False):
		super().__init__(hnd, targetProperty)
		self.addProperty(angle)
	def toBlockString(self):
		hnd		= self.getHandle()
		aHnd	= hnd + "-deg"
		output	= aHnd + ":" + self.getPropertyString(0) + ";\n"
		output	+= hnd + "-0: var(" + aHnd + ");\n";
		output	+= hnd + "-1: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 6);\n"
		output	+= hnd + "-2:  calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 120);\n"
		output	+= hnd + "-3:  calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 5040);\n"
		output	+= hnd + "-4: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 362880);\n"
		output	+= hnd + ": calc(var(" +  hnd + "-0) - var(" +  hnd + "-1)  + var(" +  hnd + "-2) - var(" +  hnd + "-3) + var(" +  hnd + "-4));\n"
		return output

		# // Sine function representation
		# .sin {
		  # --sin1: var(" + aHnd + ");
		  # --sin2: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 6);
		  # --sin3: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 120);
		  # --sin4: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 5040);
		  # --sin5: calc((var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ")) / 362880);
		  # --sin: calc(var(--sin1) - var(--sin2) + var(--sin3) - var(--sin4) + var(--sin5));
		# }
	