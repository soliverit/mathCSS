import numpy as np
from sklearn.ensemble 		import GradientBoostingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing	
class CSSModeller():
	
	def __init__(self, data, target, trainTestSplit=0.5):
		self.data   			= data
		self.headers			= [header for header in data.head() if header != target]
		self.target 			= target
		self.trainTestSplit		= trainTestSplit
		self.trainingData		= False
		self.trainingTargets	= False
		self.testData			= False
		self.testTargets		= False
		##
		# Scaling and normalisation parameters
		##
		self.normaliseData		= True
		self.normaliseTargets	= False
		self.updateData(self.data)
	def updateData(self, data):
		self.data				= data
		# Temp data
		targets					= data[self.target]
		data					= data.drop(labels=self.target, axis=1)	
		# Do training data
		self.trainingData		= data[int(len(data) * self.trainTestSplit):]
		self.trainingTargets	= np.array(targets[int(len(data) * self.trainTestSplit):])		
		# Do test data
		self.testData			= data[:int(len(data) * (1 - self.trainTestSplit))]
		self.testTargets		= np.array(targets[:int(len(data) * (1 - self.trainTestSplit))])
		
		print(len(self.data))
		print(len(self.trainingData))
		print(len(self.testData))
	##
	# Get the number of entries in the training data
	##
	def trainingDataLength(self):
		return len(self.trainingData)
	##
	# Get the number of entries in the test data
	##
	def testDataLength(self):
		return len(self.testData)
	def extractData(self, data):
		min_max_scaler = preprocessing.MinMaxScaler()
		return min_max_scaler.fit_transform(data)
	def getTrainingData(self):
		if not self.normaliseData:
			return self.testData
		return self.extractData(self.trainingData)
	def getTestData(self):
		if not self.normaliseData:
			return self.testData
		return self.extractData(self.testData)
	def getTrainingTargets(self):
		if not self.normaliseTargets:
			return self.trainingTargets
		return self.extractData([self.trainingTargets])[0]
	def getTestTargets(self):
		if  not self.normaliseTargets:
			return self.testTargets
		return self.extractData([self.testTargets])[0]
	def printSummary(self):
		print("No. Train records: " + str(len(self.trainingData)))
		print("No. Test records: " + str(self.testDataLength()))
	def train(self):
		self.printSummary()
		# self.model	= GradientBoostingRegressor(random_state=0, learning_rate=0.05, n_estimators=200)
		self.model = MLPRegressor(
			solver=			'adam', 
			max_iter= 		10000,
			learning_rate="adaptive",
			learning_rate_init=0.01,
			alpha=			0.001,
			random_state=	1,
			hidden_layer_sizes=(len(self.headers), 2) 
		)
		self.model.fit(self.getTrainingData(), self.getTrainingTargets())
		print(self.model.score(self.getTestData(),self.getTestTargets()))


	
     
    
  