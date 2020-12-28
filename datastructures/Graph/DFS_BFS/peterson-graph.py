
from collections import defaultdict

class Graph:

	def __init__(self):

		self.root = -1
		self.V = 0
		self.graph = defaultdict(list)
		self.path = []

	def addEdge(self, src, dest):

		if src not in self.graph:
			self.V += 1
		if dest not in self.graph:
			self.V += 1

		self.graph[src].append(dest)
		self.graph[dest].append(src)


	def findWalk(self, string):

		self.root = (ord(string[0]) - ord('A')) % 5

		count = 0
		path  = []
		self.DFS(self.root, count, string, path)
		
		if len(path) != len(string):
			print(-1)
		else:
			for i in path:
				print(i, end='')
	def DFS(self, src, count, string, path):

		
		ch = chr(ord('A') + (src % 5))
		if count == len(string) or ch != string[count]:
			return

		path.append(src)

		for i in self.graph[src]:

			self.DFS(i, count + 1, string, path)


graph = Graph()

graph.addEdge(0, 4)
graph.addEdge(0, 5)
graph.addEdge(0, 1)
graph.addEdge(4, 9)
graph.addEdge(4, 3)
graph.addEdge(3, 8)
graph.addEdge(3, 2)
graph.addEdge(2, 7)
graph.addEdge(2, 1)
graph.addEdge(1, 6)
graph.addEdge(6, 9)
graph.addEdge(6, 8)
graph.addEdge(5, 8)
graph.addEdge(5, 7)
graph.addEdge(7, 9)

graph.findWalk('AADDCB')