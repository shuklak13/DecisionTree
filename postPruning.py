from random import randint
from copy import deepcopy
from ID3 import *

#L = number of trees to compare
#K = maximum number of pruning attempts per tree
def postPruning(L, K, dTree, testExamples):
	bestDTree = dTree
	for i in range(0,L):
		newDTree = deepcopy(dTree)
		M = randint(1, K)
		for j in range(0, M):
			nonLeafNodes = newDTree.getNonLeafNodes()
			P = randint(0, len(nonLeafNodes) - 1)
			nonLeafNodes[P].prune()
		if newDTree.accuracy(testExamples) > bestDTree.accuracy(testExamples):
			bestDTree = newDTree
	return bestDTree
