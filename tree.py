class node(object):
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