from random import randint
from copy import deepcopy
from ID3 import *

def postPruning(L, K, dTree, testExamples):
	bestDTree = dTree
	for i in range(1,L+1):
		newDTree = deepcopy(dTree)
		M = randint(1, K)
		for j in range(1, M+1):
			nonLeafNodes = newDTree.getNonLeafNodes()
			P = randint(0, len(nonLeafNodes) - 1)
			nonLeafNodes[P].prune()
		if accuracy(newDTree) > accuracy(bestDTree):
			bestDTree = newDTree
	return bestDTree
