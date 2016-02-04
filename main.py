#Currently need to:
#	test bestClassifier
#	test splitExamples
#	fix print out

#run with
#python assignment1.py 0 0 training_set.csv validation_set.csv test_set.csv yes

from sys import argv
import csv
from ID3 import *

##############################################################################

L = argv[1]	#used in post-pruning
K = argv[2]	#used in post-pruning

attributes = []

trainingSetFile = csv.reader(open(argv[3], 'r'))
trainingSet = []	#list of lists (2D Array!)
for example in trainingSetFile:
	if len(attributes) == 0:
		attributes = example
	else:
		trainingSet.append(example)

dTree = DecisionTree(attributes, trainingSet)
dTree.printOut()

validationSet = argv[4]
testSet = argv[5]
toPrint = argv[6]	#yes or no