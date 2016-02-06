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
#	print "Positive: " + str(positive) + \
#		"\tNegative: " + str(size - positive) + \
#		"\tTotal: " + str(size)
	return {"Positive": positive, 
		"Negative": size - positive, "Total": size}

#splits example and removes split attribute
def splitExamples(examples, attrIndex):
	posEx = []
	negEx = []
	for example in examples:
		attrVal = example[attrIndex]
		if attrVal == "0":
			negEx.append(example)
		if attrVal == "1":
			posEx.append(example)
	return {"Positive": posEx, "Negative": negEx}