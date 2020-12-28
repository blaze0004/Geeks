
from Graph import DirectedGraph

class UnionFindByRank(DirectedGraph):
	"""docstring for UnionFindByRank"""
	def __init__(self):
		super(UnionFindByRank, self).__init__()

	def find(self, parent, elem):
		
		if parent[elem] == -1: return elem
		return self.find(parent, parent[elem])

	def union(self, parent, elem1, elem2):
		
		parent_elem1 = self.find(parent, elem1)
		parent_elem2 = self.find(parent, elem2)

		parent[parent_elem1] = parent_elem2

	def isCycle(self, src):

		parent = {key: -1 for key, _ in self.graph.items()}

		for src in self.graph:

			for dest in self.graph[src]:

				parent_src = self.find(parent, src)
				parent_dest = self.find(parent, dest)

				if parent_src == parent_dest:

					return True

				self.union(parent, parent_src, parent_dest)

		return False

graph = UnionFindByRank()

edges = [(0, 1), (1, 2), (2, 0)]

for src, dest in edges:
	graph.addEdge(src, dest)

print(graph.isCycle(0))