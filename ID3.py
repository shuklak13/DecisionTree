from ID3supplementalFunctions import *
from testingForTermination import *
from bestClassifier import *

#binary tree, attributes will only have values 0, 1
	#So I don't need all that dictionary magic
class DecisionTree(object):
	def __init__(self, attributes, trainingSet, heuristicAlgo = calculateEntropy, level=0):
		self.level = level
		print "level " + str(level)
		self.attributes = attributes
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
		for example in childrenExamples["Positive"]:
			example.remove(decisAttrIndex)
		for example in childrenExamples["Negative"]:
			example.remove(decisAttrIndex)	
			
		childrenAttributes = attributes
		childrenAttributes.remove(self.decisionAttribute)
		
		leftChild = DecisionTree(childrenAttributes,
					childrenExamples["Positive"], level=self.level+1)
		rightChild = DecisionTree(childrenAttributes, 
					childrenExamples["Negative"], level=self.level+1)
			
		return [leftChild, rightChild]
		
		
	def isLeaf(self):
		if self.children is None:
			return True
		else:
			return False

	#I KNOW this doesn't work lol, fix later
	def printOut(self):
		print self.__repr__()
	def __repr__(self):
		if self.isLeaf():
			output = self.classification
		else:
			output = "\n" + "| "*self.level + self.decisionAttribute + " = : "
			for child in self.children:
				output += child.__repr__()
			
		return output
		