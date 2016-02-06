from ID3supplementalFunctions import *

def testForTermination(attributes, trainingSet):
	uniformityResults = testUniformity(trainingSet)
	if uniformityResults is not False:
		return uniformityResults
	print "The tree is not uniform"

	attributesResults = testAttributes(attributes, trainingSet)
	if attributesResults is not False:
		return attributesResults
		
	return False

#tests if all examples are positive or negative
def testUniformity(trainingSet):
	numberOf = countPositiveNegativeTotal(trainingSet)
	if 	numberOf["Positive"] == numberOf["Total"]:	return "Positive"
	elif numberOf["Negative"] == numberOf["Total"]:	return "Negative"
	else:	return False

#tests if there is all attributes have been exhausted
def testAttributes(attributes, trainingSet):
	if len(attributes) <= 1:
		return positiveOrNegative(trainingSet)
	return False