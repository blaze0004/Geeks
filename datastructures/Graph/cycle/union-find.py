
from Graph import DirectedGraph

class UnionFind(DirectedGraph):
	"""docstring for UnionFind"""
	def __init__(self):
		super(UnionFind, self).__init__()
	
	def unionFind(self, parent, i):
		if parent[i] == -1:
			return i
		return self.unionFind(parent, parent[i])

	def union(self, parent, x, y):

		xset = self.unionFind(parent, x)
		yset = self.unionFind(parent, y)
		parent[xset] = yset


	def findCycle(self):

		parent = [-1] * (self.V)

		for src in self.graph:

			for dest in self.graph[src]:

				x = self.unionFind(parent, src)
				y = self.unionFind(parent, dest)
				# print(x, y)
				if x == y:

					return True

				self.union(parent, x, y)


graph = UnionFind()

graph.addEdge(0, 1)
graph.addEdge(1, 2)
graph.addEdge(2, 0)
# print(graph.graph)
# print(graph.V)

print(graph.findCycle())