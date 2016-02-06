import random

def postPruning(L, K, dTree):
	bestDTree = dTree
	for i in range(1,L+1):
		newDTree = dTree
		M = random.randint(1, K)
		for j in range(1, M+1):
			N = newDTree.numNonLeafNodes()
			P = random.randint(1, N)
			newDTree.pruneNode(P)
		if(accuracy(newDTree) > accuracy(bestDTree):
			bestDTree = newDTree
	return bestDTree