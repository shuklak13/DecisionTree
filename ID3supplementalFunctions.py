from math import log

def bestClassifier(attributes, trainingExamples):
	entropy = calculateEntropy(trainingExamples)
	gainz = []
	for attrIndex in 0:(length(attributes)-1):
		childrenExamples = splitExamples(trainingExamples, attrIndex)
		gain = entropy 
			- length(childrenExamples["Positive"]) / length(trainingExamples)
				* calculateEntropy(childrenExamples["Positive"])
			- length(childrenExamples["Negative"]) / length(trainingExamples)
				* calculateEntropy(childrenExamples["Negative"])
		gainz.append(gain)
	maxGainz = gainz.index(max(gainz))
	return attributes[maxGainz]
		
def calculateEntropy(trainingExamples):
	numberOf = countPositiveNegativeTotal(trainingExamples)
	pPos = numberOf["Positive"] / numberOf["Total"]
	pNeg = numberOf["Negative"] / numberOf["Total"]
	return -(pPos * log(pPos, 2) + pNeg * log(pNeg, 2))
		
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

#splits example and removes split attribute
def splitExamples(examples, attrIndex):
	posEx = []
	negEx = []
	for example in examples:
		attrVal = example.pop(attrIndex)
		if attrVal = "0":
			negEx.append(example)
		if attrVal = "1":
			posEx.append(example)
      return {"Positive": posEx, "Negative": negEx}


from testingForTermination.py import *