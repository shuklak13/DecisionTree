from genericTree import tree

#creates and returns a decision tree created from training set on attributes
#def ID3algo(attributes, trainingSet):
#	uniformityResults = testUniformity(trainingSet)
#	if uniformityResults is not None:
#		return uniformityResults
#
#	attributesResults = testAttributes(attributes, trainingSet)
#	if attributesResults is not None:
#		return attributesResults
#
#	#ADD ID3 ALGO HERE
#	A = bestClassifier()
#	
#	return dTree
	
def bestClassifier():
	

def testUniformity(trainingSet):
	uniformity = isUniform(trainingSet)
	if uniformity is not False:
		if uniformity == "Positive":
			return decisionTree(1)
		if uniformity == "Negative":
			return decisionTree(0)
	return None

def testAttributes(attributes, trainingSet):
	if len(attributes) <= 1:
		polarity = positiveOrNegative(trainingSet)
		if polarity == "Positive":
			return decisionTree(1)
		if polarity == "Negative":
			return decisionTree(0)
	return None

def isUniform(trainingSet):
	numberOf = countPositiveNegativeTotal(trainingSet)
	if 		numberOf["Positive"] == numberOf["Total"]:	return "Positive"
	elif 	numberOf["Negative"] == numberOf["Total"]:	return "Negative"
	else:												return False

def positiveOrNegative(examples):
	numberOf = countPositiveNegativeTotal(examples)
	if numberOf["Positive"] > numberOf["Negative"]:
		return "Positive"
	else:
		return "Negative"

def countPositiveNegativeTotal(examples):
	size = 0
	positive = 0
	for example in examples:
		size += 1
		if example[-1] == "1":
			positive += 1
	return {"Positive": positive, 
		"Negative": size - positive, "Total": size}

class DecisionTree(Tree):
	def __init__(self, decisionAttribute = None, attributes, value):
		self.decisionAttribute = decisionAttribute
		self.attributes = attributes
		Tree.__init__(self, value)
		
		uniformityResults = testUniformity(trainingSet)
		if uniformityResults is not None:
			return uniformityResults
	
		attributesResults = testAttributes(attributes, trainingSet)
		if attributesResults is not None:
			return attributesResults
	
		#ADD ID3 ALGO HERE
		A = bestClassifier()
		