from collections import defaultdict

class DirectedGraph:

	def __init__(self):

		self.V = 0
		self.graph = defaultdict(list)
		self.root = -1

	def addEdge(self, src, dest):

		if src not in self.graph:
			self.V += 1

		self.graph[src].append(dest)

	def printGraph(self):
		for k,v in self.graph.items():
			print(k, ' -> ', v)

class UnDirectedGraph:

	def __init__(self):

		self.V = 0
		self.graph = defaultdict(list)
		self.root = -1

	def addEdge(self, src, dest):

		if src not in self.graph:
			self.V += 1
		if dest not in self.graph:
			self.V += 1

		self.graph[src].append(dest)
		self.graph[dest].append(src)

	def printGraph(self):
		for k,v in self.graph.items():
			print(k, ' -> ', v)
