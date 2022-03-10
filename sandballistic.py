## Includes
# Native
from random import randint
# Project
from lib.css_blocks.sum					import Sum
from lib.css_blocks.power				import Power
from lib.css_blocks.product				import Product
from lib.css_blocks.sqrt				import Sqrt
from lib.css_blocks.sin					import Sin
from lib.css_blocks.cos					import Cos
from lib.css_blocks.tan					import Tan
from lib.css_blocks.distance			import Distance
from lib.css_blocks.ballistic_formula	import BallisticFormula
from lib.css_property					import CSSProperty
from lib.html_document					import HTMLDocument
from lib.html_objects.graph				import Graph
from lib.html_objects.series			import Series


## Some data
GRAVITY 	= CSSProperty("gravity", 8.)
GRAVITY_2	= CSSProperty("gravity_2", 5.5)
VELOCITY	= CSSProperty("velocity", 57)
VELOCITY_2	= CSSProperty("velocity", 57)

## Some data points for the graph
series	= []
line	= []
for idx in range(15):
	line.append(BallisticFormula("ballistic-line" + str(idx), CSSProperty("-lx-" + str(idx), idx), GRAVITY, VELOCITY, "bottom"))
	series.append(BallisticFormula("ballistic-series" + str(idx), CSSProperty("-sx-" + str(idx), idx), GRAVITY_2, VELOCITY_2, "bottom"))

## The graph
html	= HTMLDocument()
graph	= Graph("the-graph", [Series(series, "green", 15), Series(line, "red", 30)])
html.addObject(graph)
print("--- HTML ---")
# print(graph.html)
print("--- CSS ---")
# print(graph.css)
## The files
html.writeHTML("./quad_graph.html")
html.writeCSS("./test/style.css")























