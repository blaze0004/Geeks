

from collections import defaultdict

class Graph:

	def __init__(self):
		self.V = 0
		self.graph = defaultdict(list)

	def addEdge(self, src, dest):

		if src not in self.graph:
			self.V += 1
		if dest not in self.graph:
			self.V += 1

		self.graph[src].append(dest)
		self.graph[dest].append(src)

	def findTrees(self, src):
		#print(self.V)
		self.visited = dict({(i, False) for i in self.graph})

		treesCount = 0
		self.visited[src] = True
		self.DFS(src)
		treesCount += 1
		for v in self.graph:

			if not self.visited[v]:

				self.visited[v] = True
				self.DFS(v)

				treesCount += 1

		return treesCount

	def DFS(self, src):

		self.visited[src] = True

		for i in self.graph[src]:
			if not self.visited[i]:
				self.DFS(i)

graph = Graph()

graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(3, 4)

print('Total number of trees in forest are: {}'.format(graph.findTrees(0)))