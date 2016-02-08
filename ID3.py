from ID3supplementalFunctions import *
from testingForTermination import *
from bestClassifier import *
from copy import deepcopy

class DecisionTree(object):
	def __init__(self, attributes = None, trainingSet = None,
							heuristicAlgo = calculateEntropy, level=0):
		self.level = level
		self.attributes = attributes
		self.examples = trainingSet
		
		terminate = testForTermination(attributes, trainingSet)
		if terminate is not False:
			self.decisionAttribute = None
			self.classification = terminate
			self.children = None
		else:
			self.decisionAttribute = bestClassifier(self.attributes, trainingSet)
			self.classification = None
			self.children = self.createChildren(deepcopy(trainingSet))
			
	def createChildren(self, trainingSet):	
		
		decisAttrIndex = self.attributes.index(self.decisionAttribute)
		
		childrenExamples = splitExamples(trainingSet, decisAttrIndex)
		for example in childrenExamples["0"]:
			del example[decisAttrIndex]
		for example in childrenExamples["1"]:
			del example[decisAttrIndex]
			
		childrenAttributes = deepcopy(self.attributes)
		childrenAttributes.remove(self.decisionAttribute)
		
		leftChild = DecisionTree(childrenAttributes,
					childrenExamples["0"], level=self.level+1)
		rightChild = DecisionTree(childrenAttributes, 
					childrenExamples["1"], level=self.level+1)
			
		return [leftChild, rightChild]
		
	def prune(self):
		self.children = None
		self.classification = positiveOrNegative(self.examples)
		
	def classify(self, instance):
		if not self.isLeaf():
			#print "Have attributes " + str(self.attributes)
			#print "Decision attribute " + self.decisionAttribute
			decAttrIndex = self.attributes.index(self.decisionAttribute)
			instanceValue = instance[decAttrIndex]
			del instance[decAttrIndex]
			if instanceValue == "0":
				return self.children[0].classify(instance)
			if instanceValue == "1":
				return self.children[1].classify(instance)
		return self.classification
		
	def accuracy(self, testExamples):
		correct = 0.0
		total = 0.0
		for example in testExamples:
			total += 1
			if self.classify(deepcopy(example)) == example[-1]:
				correct += 1
		return correct/total
	
	def getNonLeafNodes(self):
		nodes = [self]
		if not self.isLeaf():
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
						" = 0: " + self.children[0].__repr__() +
					"\n" + "| "*self.level + self.decisionAttribute + 
						" = 1: " + self.children[1].__repr__())
			
		return output
	