from ID3supplementalFunctions import *

#binary tree, attributes will only have values 0, 1
	#So I don't need all that dictionary magic
class DecisionTree(Tree):
	def __init__(self, attributes, trainingSet):
		self.attributes = attributes
		
		terminate = testForTermination(attributes, trainingSet)
		if terminate is not False:
			return terminate
	
		self.decisionAttribute = bestClassifier()	#incomplete
		
		childrenExamples = splitExamples(trainingSet, 
						attributes.index(self.decisionAttribute))
						
		childrenAttributes = attributes
		childrenAttributes.remove(self.decisionAttribute)
		
		self.children = [DecisionTree(childrenAttributes, childrenExamples["Positive"]),
					DecisionTree(childrenAttributes, childrenExamples["Negative"])]
		
		#MAKE NEW CHILD FOR EACH SPLIT EXAMPLE
		
		