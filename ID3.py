from ID3supplementalFunctions import *

#binary tree, attributes will only have values 0, 1
	#So I don't need all that dictionary magic
class DecisionTree(Tree):
	def __init__(self, attributes, trainingSet):
		
		self.attributes = attributes
		
		terminate = testForTermination(attributes, trainingSet)
		if terminate is not False:
			return terminate
	
		self.decisionAttribute = bestClassifier()
		self.classification = positiveOrNegative(trainingSet)
		
		self.children = createChildren(attributes, trainingSet)
		
		
	def createChildren(self, attributes, trainingSet):
		childrenExamples = splitExamples(trainingSet, 
						attributes.index(self.decisionAttribute))
						
		childrenAttributes = attributes
		childrenAttributes.remove(self.decisionAttribute)
		
		self.children = createChildren(attributes, trainingSet)
		
		if length(childrenExamples["Positive"])==0:
			leftChild = positiveOrNegative(trainingSet)
		else:
			leftChild = DecisionTree(childrenAttributes, childrenExamples["Positive"])
			
		if length(childrenExamples["Negative"])==0:
			rightChild = positiveOrNegative(trainingSet)
		else:
			rightChild = DecisionTree(childrenAttributes, childrenExamples["Negative"])
			
		return [leftChild, rightChild]
		

	#I KNOW this doesn't work lol, fix later
	def printOut(self, level=0):
		print self.__repr__(level)
	def __repr__(self, level=0):
		output = "| "*level + self.decisionAttribute + " = : " + self.classification + "\n"
		for child in self.children:
			output += child.__repr__(level+1)
		return output