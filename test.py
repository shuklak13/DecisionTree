import os; os.chdir("C:\Users\Karan\SkyDrive\School\MachineLearning\hw1")
import csv
from ID3 import *
import bestClassifier

attributes = []

trainingSetFile = csv.reader(open("training_set4.csv", 'r'))
trainingSet = []	#list of lists (2D Array!)
for example in trainingSetFile:
	if len(attributes) == 0:
		attributes = example
	else:
		trainingSet.append(example)

dTree = DecisionTree(attributes, trainingSet)
dTree.printOut()

dTreeVI = DecisionTree(attributes, trainingSet, bestClassifier.calculateVarianceImpurity)
dTreeVI.printOut()