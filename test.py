import os; os.chdir("C:\Users\Karan\SkyDrive\School\MachineLearning\hw1")
import csv
from ID3 import *
from bestClassifier import calculateVarianceImpurity
from postPruning import *

attributes = []

trainingSetFile = csv.reader(open("training_set.csv", 'r'))
trainingSet = []	#list of lists (2D Array!)
for example in trainingSetFile:
	if len(attributes) == 0:
		attributes = example
	else:
		trainingSet.append(example)
		
testSetFile = csv.reader(open("test_set.csv", 'r'))
testSet = []
for example in testSetFile:
	testSet.append(example)
del testSet[0]

dTree = DecisionTree(attributes, trainingSet)
#dTree.printOut()
print str(dTree.accuracy(testSet))

dTree = postPruning(20, 20, dTree, testSet)
#dTree.printOut()
print str(dTree.accuracy(testSet))

dTreeVI = DecisionTree(attributes, trainingSet, calculateVarianceImpurity)
#dTreeVI.printOut()
print str(dTreeVI.accuracy(testSet))

dTreeVI = postPruning(20, 20, dTreeVI, testSet)
#dTreeVI.printOut()
print str(dTree.accuracy(testSet))