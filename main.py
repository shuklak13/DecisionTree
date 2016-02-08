#Currently need to:
#	test accuracy
#	test postPruning
#	 	doesn't seem to show any accuracy improvements?
#	 	bestTree is probably not being replaced???
#	fix accuracy on variance impurity method (gives bad result on training set 4)

#change directory with
#cd C:\Users\Karan\SkyDrive\School\MachineLearning\hw1
	#or
#import os; os.chdir("C:\Users\Karan\SkyDrive\School\MachineLearning\hw1")

#run with
#python assignment1.py 20 20 training_set.csv validation_set.csv test_set.csv no

from sys import argv
import csv
from ID3 import *
from bestClassifier import calculateVarianceImpurity
from postPruning import *

##############################################################################

attributes = []

trainingSetFile = csv.reader(open(argv[3], 'r'))
trainingSet = []	#list of lists (2D Array!)
for example in trainingSetFile:
	if len(attributes) == 0:
		attributes = example
	else:
		trainingSet.append(example)
		
validationSetFile = csv.reader(open(argv[4], 'r'))
validationSet = []
for example in validationSetFile:
	validationSet.append(example)
del validationSet[0]
		
testSetFile = csv.reader(open(argv[5], 'r'))
testSet = []
for example in testSetFile:
	testSet.append(example)
del testSet[0]

L = int(argv[1])	#used in post-pruning
K = int(argv[2])	#used in post-pruning

dTree = DecisionTree(attributes, trainingSet)
dTreePruned = postPruning(L, K, dTree, validationSet)
dTreeVI = DecisionTree(attributes, trainingSet, calculateVarianceImpurity)
dTreeVIPruned = postPruning(L, K, dTreeVI, validationSet)

toPrint = argv[6]	#yes or no

if toPrint == "yes":
	dTree.printOut()
	dTreeVI.printOut()