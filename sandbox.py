from lib.css_blocks.sum							import Sum
from lib.css_blocks.power						import Power
from lib.css_blocks.product						import Product
from lib.css_blocks.sqrt						import Sqrt
from lib.css_blocks.sin							import Sin
from lib.css_blocks.cos							import Cos
from lib.css_blocks.tan							import Tan
from lib.css_blocks.distance					import Distance
from lib.css_blocks.simple_linear_regression	import SimpleLinearRegression
from lib.css_property							import CSSProperty
from lib.html_document							import HTMLDocument

def printBlock(name, block):
	print("--- " + name + " ---")
	print(str(block).replace("\n", "\n\t").replace("\t}","}"))
	print("-----------------------")
	
## Properties
a		= CSSProperty("a", 30)
b		= CSSProperty("	b", 40)
deg		= CSSProperty("angle", 45)
x		= [CSSProperty("x1", 30), CSSProperty("x2", 5), CSSProperty("x3", 4), CSSProperty("x3", 5), CSSProperty("x3", 4)]
y		= [CSSProperty("y1", 3), CSSProperty("y2", 7), CSSProperty("y3", 12), CSSProperty("x3", 15), CSSProperty("x3", 12)]

html	= HTMLDocument()

html.write("./page.html")


























## Objects
sum		= Sum("sum", x, 'height')
power	= Power("power", a, b, 'height')
product	= Product("product", x, 'height')
sqrt	= Sqrt("sqrt", a, 'height')
sin		= Sin("sin", deg, 'height')
cos		= Cos("cos", deg, 'height')
tan		= Tan("tan", deg, 'height')
dist	= Distance("dist", a, b, 'height')
lin		= SimpleLinearRegression("slg", x, y, 'height')

## Debug
print("Let's do this")
printBlock("SUM", sum)
# printBlock("POWER", power)
# printBlock("PRODUCT", product)
# printBlock("SQRT", sqrt)
# printBlock("SIN", sin)
# printBlock("COS", cos)
# printBlock("TAN", tan)
printBlock("DIST", dist)
# printBlock("Simple linear regression", lin)

## Do test stuff
page	= open("./test/page.html", "w")
css		= open("./test/style.css", "w")

css.write("\n" + str(sum))
css.write("\n" + str(product))
css.write("\n" + str(power))
css.write("\n" + str(sqrt))
css.write("\n" + str(sin))
css.write("\n" + str(cos))
css.write("\n" + str(tan))
css.write("\n" + str(lin))
css.close()

page.write("<html><body><div id='parent'>")
page.write("<span width='300px' id='" + sum.getBlockID() + "'>&nbsp;</span>")
page.write("<div width='300px' id='" + product.getBlockID() + "'>&nbsp;</div>")
page.write("<div width='300px' id='" + power.getBlockID() + "'>&nbsp;</div>")
page.write("<div width='300px' id='" + sqrt.getBlockID() + "'>&nbsp;</div>")
page.write("<div width='300px' id='" + sin.getBlockID() + "'>&nbsp;</div>")
page.write("<div width='300px' id='" + cos.getBlockID() + "'>&nbsp;</div>")
page.write("<div width='300px' id='" + tan.getBlockID() + "'>&nbsp;</div>")
page.write("<div width='300px' id='" + lin.getBlockID() + "'>&nbsp;</div>")
# page.write("<div width='300px' id='" + sum.getBlockID() + "'>&nbsp;</div>")
# page.write("<div width='300px' id='" + product.getBlockID() + "'>&nbsp;</div>")
# page.write("<div width='300px' id='" + power.getBlockID() + "'>&nbsp;</div>")
# page.write("<div width='300px' id='" + sqrt.getBlockID() + "'>&nbsp;</div>")
# page.write("<div width='300px' id='" + sin.getBlockID() + "'>&nbsp;</div>")
# page.write("<div width='300px' id='" + cos.getBlockID() + "'>&nbsp;</div>")
# page.write("<div width='300px' id='" + tan.getBlockID() + "'>&nbsp;</div>")
# page.write("<div width='300px' id='" + lin.getBlockID() + "'>&nbsp;</div>")
page.write("</div></body></html>")
page.close()
