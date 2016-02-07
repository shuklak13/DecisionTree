from ID3supplementalFunctions import *
from testingForTermination import *
from bestClassifier import *

class DecisionTree(object):
	def __init__(self, attributes = None, trainingSet = None, heuristicAlgo = calculateEntropy, level=0):
		self.level = level
		self.attributes = attributes
		self.examples = trainingSet
		terminate = testForTermination(attributes, trainingSet)
		if terminate is not False:
			self.decisionAttribute = None
			self.classification = terminate
			self.children = None
		else:
			self.decisionAttribute = bestClassifier(attributes, trainingSet)
			self.classification = None
			self.children = self.createChildren(attributes, trainingSet)
		
		
	def createChildren(self, attributes, trainingSet):	
		
		decisAttrIndex = attributes.index(self.decisionAttribute)
		
		childrenExamples = splitExamples(trainingSet, 
						decisAttrIndex)
		for example in childrenExamples["1"]:
			del example[decisAttrIndex]
		for example in childrenExamples["0"]:
			del example[decisAttrIndex]
			
		childrenAttributes = attributes
		childrenAttributes.remove(self.decisionAttribute)
		
		leftChild = DecisionTree(childrenAttributes,
					childrenExamples["1"], level=self.level+1)
		rightChild = DecisionTree(childrenAttributes, 
					childrenExamples["0"], level=self.level+1)
			
		return [leftChild, rightChild]
		
	def prune(self):
		self.children = None
		self.classification = positiveOrNegative(self.examples)
	
	def getNonLeafNodes(self):
		nodes = [self]
		if not self.children[0].isLeaf():
			nodes.extend(self.children[0].getNonLeafNodes())
		if not self.children[1].isLeaf():
			nodes.extend(self.children[1].getNonLeafNodes())
		return nodes
		
		
	def isLeaf(self):
		if self.children is None:
			return True
		else:
			return False

	def printOut(self):
		print self.__repr__()
	def __repr__(self):
		if self.isLeaf():
			output = self.classification
		else:
			output = ("\n" + "| "*self.level + self.decisionAttribute + 
						" = 0: " + self.children[1].__repr__() +
					"\n" + "| "*self.level + self.decisionAttribute + 
						" = 1: " + self.children[0].__repr__())
			
		return output
	