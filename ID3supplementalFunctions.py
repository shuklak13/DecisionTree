#STILL NEED TO MAKE	
def bestClassifier(attributes):
	if len(attributes>1):
		return attributes[0]
	else:
		return None
		
def terminate(attributes, trainingSet):
	uniformityResults = testUniformity(trainingSet)
	if uniformityResults is not None:
		return uniformityResults

	attributesResults = testAttributes(attributes, trainingSet)
	if attributesResults is not None:
		return attributesResults
		
	return False

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
	if 	numberOf["Positive"] == numberOf["Total"]:	return "Positive"
	elif 	numberOf["Negative"] == numberOf["Total"]:	return "Negative"
	else:												return False

def positiveOrNegative(examples):
	numberOf = countPositiveNegativeTotal(examples)
	if numberOf["Positive"] > numberOf["Negative"]:
		return "Positive"
	else:
		return "Negative"

def countPositiveNegativeTotal(examples, index = -1):
	size = 0
	positive = 0
	for example in examples:
		size += 1
		if example[index] == "1":
			positive += 1
	return {"Positive": positive, 
		"Negative": size - positive, "Total": size}

#DOES THIS WORK??? TEST IT
def splitExamples(examples, index):
	posEx = []
	negEx = []
	for example in examples:
		attrVal = example.pop(index)
		if attrVal = "0":
			negEx.append(example)
		if attrVal = "1":
			posEx.append(example)
      return {"Positive": posEx, "Negative": negEx}
