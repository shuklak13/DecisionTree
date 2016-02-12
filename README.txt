Karan Shukla

The program was created and run on Windows 8.1's command line. It is a Python 2.7.10 program.

The program accepts command line arguments in the following manner
python main.py <L> <K> <training-set> <validation-set> <test-set> <to-print>

For example,
python main.py 10 20 training_set.csv validation_set.csv test_set.csv yes

When run, the program will print the accuracy of the four decision trees.

If run with the to-print argument set to "yes", then the program will print out the four decision trees to the console and to the files "entropyTree.txt", "entropyTreePruned.txt", "varianceImpurityTree.txt", and "varianceImpurityPrunedTree.txt".
Each file will also contain the accuracy for its decision tree.