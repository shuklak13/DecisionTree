from math import log
from ID3supplementalFunctions import countPositiveNegativeTotal, splitExamples
		
def calculateEntropy(examples):
	#print "calculating entropy"
	numberOf = countPositiveNegativeTotal(examples)
	pPos = float(numberOf["Positive"]) / float(numberOf["Total"])
	pNeg = float(numberOf["Negative"]) / float(numberOf["Total"])
	#print "pPos: " + str(pPos) + " pNeg: " + str(pNeg)
	if pPos==0:
		return -pNeg * log(pNeg, 2)
	elif pNeg==0:
		return -pPos * log(pPos, 2)
	else:
		return -(pPos * log(pPos, 2) + pNeg * log(pNeg, 2))
	
def calculateVarianceImpurity(examples):
	numberOf = countPositiveNegativeTotal(examples)
	return (numberOf["Positive"]*numberOf["Negative"]
			/
			numberOf["Total"]/numberOf["Total"] )
			
#heuristic is calculateEntropy by default
#Set to calculateVarianceImpurity to do the Variance Impurity Heuristic instead
#If a perfect split is found, halts early and returns the attribute
def bestClassifier(attributes, trainingExamples, heuristicAlgo = calculateEntropy):
	heuristic = heuristicAlgo(trainingExamples)
	gainz = []
	for attrIndex in range(len(attributes)-1):
#		print "\nChecking attribute " + str(attrIndex+1)
#		print "Number of Attributes: " + str(len(attributes)-1)
#		print "Length of examples: " + str(len(trainingExamples[0])-1)
		childrenExamples = splitExamples(trainingExamples, attrIndex)
		if isEmptyChild(childrenExamples):
			gain = 0
		else:
			gain = (
				heuristic 
				- len(childrenExamples["Positive"]) / len(trainingExamples)
					* heuristicAlgo(childrenExamples["Positive"])
				- len(childrenExamples["Negative"]) / len(trainingExamples)
					* heuristicAlgo(childrenExamples["Negative"])
					)
		gainz.append(gain)
	maxGainz = gainz.index(max(gainz))
	return attributes[maxGainz]
	
def isEmptyChild(childrenExamples):
	return (len(childrenExamples["Positive"]) == 0
			or
			len(childrenExamples["Negative"]) == 0)