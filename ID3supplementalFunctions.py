from math import log
		
def calculateEntropy(examples):
	numberOf = countPositiveNegativeTotal(examples)
	pPos = numberOf["Positive"] / numberOf["Total"]
	pNeg = numberOf["Negative"] / numberOf["Total"]
	return -(pPos * log(pPos, 2) + pNeg * log(pNeg, 2))
	
def calculateVarianceImpurity(examples):
	numberOf = countPositiveNegativeTotal(examples)
	return (numberOf["Positive"]*numberOf["Negative"]
			/
			numberOf["Total"]/numberOf["Total"] )
			
#heuristic is calculateEntropy by default
#Set to calculateVarianceImpurity to do the Variance Impurity Heuristic instead
def bestClassifier(attributes, trainingExamples, heuristicAlgo = calculateEntropy):
	heuristic = heuristicAlgo(trainingExamples)
	gainz = []
	for attrIndex in range(0, length(attributes)-1):
		childrenExamples = splitExamples(trainingExamples, attrIndex)
		gain = (
			heuristic 
			- length(childrenExamples["Positive"]) / length(trainingExamples)
				* heuristicAlgo(childrenExamples["Positive"])
			- length(childrenExamples["Negative"]) / length(trainingExamples)
				* heuristicAlgo(childrenExamples["Negative"])
				)
		gainz.append(gain)
	maxGainz = gainz.index(max(gainz))
	return attributes[maxGainz]	
		
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
		if attrVal == "0":
			negEx.append(example)
		if attrVal == "1":
			posEx.append(example)
	return {"Positive": posEx, "Negative": negEx}


from testingForTermination.py import *