from genericTree import tree

#creates and returns a decision tree created from training set on attributes
def ID3algo(trainingSet, attributes):
	print "testing uniformity"
	uniformityResults = testUniformity(trainingSet)
	if uniformityResults is not None:
		return uniformityResults

	print "testing attributes"
	attributesResults = testAttributes(attributes, trainingSet)
	if attributesResults is not None:
		return attributesResults

	print "is not uniform, has attributes"
	#ADD ID3 ALGO HERE
	return dTree

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

def positiveOrNegative(trainingSet):
	numberOf = countPositiveNegativeTotal(trainingSet)
	if numberOf["Positive"] > numberOf["Negative"]:
		return "Positive"
	else:
		return "Negative"

def countPositiveNegativeTotal(trainingSet):
	trainingSize = 0
	trainingPositive = 0
	for example in trainingSet:
		trainingSize += 1
		if example[-1] == "1":
			trainingPositive += 1
	return {"Positive": trainingPositive, 
		"Negative": trainingSize - trainingPositive, "Total": trainingSize}

class decisionTree(tree):
	attributes = []