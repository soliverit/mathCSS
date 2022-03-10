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


def printBlock(name, block):
	print("--- " + name + " ---")
	print(str(block).replace("\n", "\n\t").replace("\t}","}"))
	print("-----------------------")
	
## Some data
X, Y	= [], []
for idx in range(50):
	X.append(CSSProperty("x-" + str(idx), idx * 2))
	Y.append(CSSProperty("y-" + str(idx), idx  + randint(1, 3)))
## Some data points for the graph
series	= []
line	= []
for idx in range(50):
	line.append(SimpleLinearRegression("lin-a" + str(idx), X, Y, X[idx].value, "bottom"))
	series.append(SimpleLinearRegression("lin-" + str(idx), X, Y, idx * randint(1, 3), "bottom"))
## The graph
html	= HTMLDocument()
graph	= Graph("the-graph", [Series(series, "green"), Series(line, "red")])
html.addObject(graph)
print("--- HTML ---")
# print(graph.html)
print("--- CSS ---")
# print(graph.css)
## The files
html.writeHTML("./graph.html")
html.writeCSS("./test/style.css")























