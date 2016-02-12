from math import log
from ID3supplementalFunctions import countPositiveNegativeTotal, splitExamples
		
def calculateEntropy(examples):
	numberOf = countPositiveNegativeTotal(examples)
	pPos = float(numberOf["1"]) / float(numberOf["Total"])
	pNeg = float(numberOf["0"]) / float(numberOf["Total"])
	if pPos==0:
		return -pNeg * log(pNeg, 2)
	elif pNeg==0:
		return -pPos * log(pPos, 2)
	else:
		return -(pPos * log(pPos, 2) + pNeg * log(pNeg, 2))
	
def calculateVarianceImpurity(examples):
	numberOf = countPositiveNegativeTotal(examples)
	return (numberOf["1"]*numberOf["0"]
			/
			numberOf["Total"]/numberOf["Total"] )
			
#heuristic is calculateEntropy by default
#Set to calculateVarianceImpurity to do the Variance Impurity Heuristic instead
#If a perfect split is found, halts early and returns the attribute
def bestClassifier(attributes, trainingExamples, heuristicAlgo = calculateEntropy):
	heuristic = heuristicAlgo(trainingExamples)
	gainz = []
	for attrIndex in range(len(attributes)-1):
		childrenExamples = splitExamples(trainingExamples, attrIndex)
		if isEmptyChild(childrenExamples):
			gain = 0
		else:
			gain = (
				heuristic 
				- float(len(childrenExamples["1"])) / float(len(trainingExamples))
					* heuristicAlgo(childrenExamples["1"])
				- float(len(childrenExamples["0"])) / float(len(trainingExamples))
					* heuristicAlgo(childrenExamples["0"])
					)
		gainz.append(gain)
	maxGainz = gainz.index(max(gainz))
	return attributes[maxGainz]
	
def isEmptyChild(childrenExamples):
	return (len(childrenExamples["1"]) == 0
			or
			len(childrenExamples["0"]) == 0)