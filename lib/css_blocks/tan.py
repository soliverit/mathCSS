from ..css_block	import CSSBlock		
class Tan(CSSBlock):

	def __init__(self, hnd, angle, targetProperty=False, scale=1):
		super().__init__(hnd, targetProperty, scale)
		self.addProperty(angle)
	def toBlockString(self):
		hnd		= self.getHandle()
		aHnd	= hnd + "-deg"
		output	= aHnd + ":" + self.getPropertyString(0) + ";\n"
		output	+= hnd + "-0: var(" + aHnd + ");\n";
		output	+= hnd + "-1: calc((1/3) * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + "));\n"
		output	+= hnd + "-2: calc((2 / 15) * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ");* var(" + aHnd + "));\n"
		output	+= hnd + "-3: calc((17/315) * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + ") * var(" + aHnd + "));\n"
		hnds	= []
		for idx in range(1, 3):
			hnds.append("var(" + hnd + "-" + str(idx) + ")")
		return hnd + ": calc(" + " + ".join(hnds) + ");\n"
		
# // Tangent function representation
# .tan {
# --tan1: var(--angle);
# --tan2: calc((1/3) * var(--angle) * var(--angle) * var(--angle));
# --tan3: calc((2 / 15) * var(--angle) * var(--angle) * var(--angle) * var(--angle) * var(--angle));
# --tan4: calc((17/315) * var(--angle) * var(--angle) * var(--angle) * var(--angle) * var(--angle) * var(--angle) * var(--angle));
# --tan: calc(var(--tan1) + var(--tan2) + var(--tan3) + var(--tan4));
# }