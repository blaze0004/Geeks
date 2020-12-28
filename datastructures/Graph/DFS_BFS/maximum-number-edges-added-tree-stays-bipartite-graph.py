
from collections import defaultdict

class BipartiteGraph:

	def __init__(self):

		self.V = 0
		self.graph = defaultdict(list)
		self.root = -1

	def addEdge(self, src, dest):
		if self.root == -1:
			self.root = src
		if src not in self.graph:
			self.V += 1
		if dest not in self.graph:
			self.V += 1
		self.graph[dest].append(src)
		self.graph[src].append(dest)

	def findMaxEdges(self):

		src = self.root

		colors = [0] * 2

		visited = {i:False for i in self.graph.keys()}
		#print(visited)
		self.DFS(src, colors, 0, visited)

		return colors[0] * colors[1] - (self.V - 1)

	def DFS(self, src, colors, color, visited):

		colors[color] += 1
		visited[src] = True

		for i in self.graph[src]:

			if not visited[i]:
				self.DFS(i, colors, not color, visited)


graph = BipartiteGraph()

graph.addEdge(1, 2)
graph.addEdge(1, 3)
graph.addEdge(2, 4)
graph.addEdge(3, 5)

print(graph.findMaxEdges())