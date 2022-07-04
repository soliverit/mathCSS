
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
from lib.css_blocks.neural_network				import NeuralNetwork
from lib.css_blocks.simple_linear_regression	import SimpleLinearRegression
from lib.css_property							import CSSProperty
from lib.html_document							import HTMLDocument
from lib.html_objects.graph						import Graph
from lib.html_objects.series					import Series
from os import chdir
from os import system
# system("cls")
chdir("c:/repos/css_building_load_prediction")
HIDDEN	= [
	{"first": -1, "second": 0, "first_node": 0, "second_node": 0, "weight": 34.4, "bias": 2.14},
	{"first": -1, "second": 0, "first_node": 0, "second_node": 1, "weight": -2.5, "bias": 1.29}
]
OUTPUT	= [
	{"first": 0, "second": 1, "first_node": 0, "second_node": 0, "weight": -1.3, "bias": 0},
	{"first": 0, "second": 1, "first_node": 1, "second_node": 0, "weight": 2.28, "bias": 0}
]
## Do the network.

## The graph
prefix	= "sin"			
XLabels	= ["dosage"]
html	= HTMLDocument(prefix)
ann		= NeuralNetwork("StatQuest-NN", ["dosage"], ["efficacy"], "shoe-NN")
ann.createHiddenLayer(2)
ann.superCoolPrint()
# ann.printConnectors()
ann.tuneConnectors(HIDDEN)
ann.tuneConnectors(OUTPUT)

print(ann.toBlockString())
print("--- HTML ---")
# print(graph.html)
print("--- CSS ---")
# print(graph.css)
## The files
html.writeHTML("./sin_graph.html")
html.writeCSS("./test/%s_style.css" %(prefix))























