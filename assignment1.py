#Currently need to:
#	test ID3, see if it makes a minimalist decision tree
#	add ID3 algo

#run with
#python assignment1.py 0 0 training_set.csv validation_set.csv test_set.csv yes

from sys import argv
import csv
from genericTree import *
from ID3 import *

##############################################################################

L = argv[1]	#used in post-pruning
K = argv[2]	#used in post-pruning

attributes = []

trainingSetFile = csv.reader(open(argv[3], 'r'))
trainingSet = []
for example in trainingSetFile:
	if len(attributes) == 0:
		attributes = example
	trainingSet.append(example)

dTree = ID3algo(attributes, trainingSet)
dTree.printOut()

validationSet = argv[4]
testSet = argv[5]
toPrint = argv[6]	#yes or no