#run with
#python main.py 20 20 training_set.csv validation_set.csv test_set.csv yes

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

print "Entropy Tree Accuracy:"
dTreeAcc = str(dTree.accuracy(testSet))
print dTreeAcc

print "\nEntropy Tree (Pruned) Accuracy:"
dTreePrunedAcc = str(dTreePruned.accuracy(testSet))
print dTreePrunedAcc

print "\nVariance Impurity Tree Accuracy:"
dTreeVIAcc = str(dTreeVI.accuracy(testSet))
print dTreeVIAcc

print "\nVariance Impurity Tree (Pruned) Accuracy:"
dTreeVIPrunedAcc = str(dTreeVIPruned.accuracy(testSet))
print dTreeVIPrunedAcc

if toPrint == "yes":
	print "\nEntropy Tree"
	dTreePrint = dTree.__repr__()
	print dTreePrint
	open("entropyTree.txt", 'w').write(dTreeAcc+"\n"+dTreePrint)
	
	print "\nEntropy (Purity) Tree"
	dTreePrunedPrint = dTreePruned.__repr__()
	print dTreePrunedPrint
	open("entropyTreePruned.txt", 'w').write(dTreePrunedAcc+"\n"+dTreePrunedPrint)
	
	print "\nVariance Impurity Tree"
	dTreeVIPrint = dTreeVI.__repr__()
	print dTreeVIPrint
	open("varianceImpurityTree.txt", 'w').write(dTreeVIAcc+"\n"+dTreeVIPrint)
	
	print "\nVariance Impurity (Pruned) Tree"
	dTreeVIPrunedPrint = dTreeVIPruned.__repr__()
	print dTreeVIPrunedPrint
	open("varianceImpurityPrunedTree.txt", 'w').write(dTreeVIPrunedAcc+"\n"+dTreePrunedPrint)