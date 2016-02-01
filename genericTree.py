class tree(object):
	def __init__(self, value, children = []):
		self.value = value
		self.children = children

	#use to print
	def printOut(self, level=0):
		print self.__repr__(level)
	def __repr__(self, level=0):
		output = "\t"*level+repr(self.value)+"\n"
		for child in self.children:
			output += child.__repr__(level+1)
		return output

	#use to insert children
	#to insert multiple, add them as a list
	def insert(self, item):
		if type(item) in [list, tuple]:
			self.children.extend(item)
		else:
			self.children.append(item)

# Example
# familytree = tree("grandmother", [
#     tree("daughter", [
#         tree("granddaughter"),
#         tree("grandson")]),
#     tree("son", [
#         tree("granddaughter"),
#         tree("grandson")])
#     ]);
# familytree.printOut()