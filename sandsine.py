## Includes
# Native
from random import randint
# Project
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
from lib.html_objects.graph						import Graph
from lib.html_objects.series					import Series


## Some data points for the graph
cos	= []
sin	= []
for idx in range(5000	):
	sin.append(Sin("sin-a" + str(idx), CSSProperty("s",float(10 +  idx/180.0)), "top", 0.01))
	cos.append(Cos("cos-a" + str(idx), CSSProperty("s", float(10 + idx/180.0)), "top", 0.01))
## The graph
prefix	= "sin"			
html	= HTMLDocument(prefix)
graph	= Graph("the-graph", [Series(sin, "green", 0.1), Series(cos, "red", 0.1)])
html.addObject(graph)
print("--- HTML ---")
# print(graph.html)
print("--- CSS ---")
# print(graph.css)
## The files
html.writeHTML("./sin_graph.html")
html.writeCSS("./test/%s_style.css" %(prefix))























