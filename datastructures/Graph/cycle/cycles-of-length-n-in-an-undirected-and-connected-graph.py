#cycles-of-length-n-in-an-undirected-and-connected-graph

from Graph import UnDirectedGraph

class CycleOfLengthN(UnDirectedGraph):

	def __init__(self):
		UnDirectedGraph.__init__(self)
		# print(self.graph)

	def countCycles(self, root, n):
		# print(self.graph)
		visited = [False] * (self.V + 1)
		# print(visited)
		self.count = 0
		for i in range(self.V - (n - 1)):

			if not visited[i]:

				self.DFS(i,i,n - 1, visited)
				visited[i] = True
		count = self.count // 2
		del self.count
		return count

	def DFS(self, src, parent, n, visited):

		visited[src] = True
		if n == 0:

			visited[src] = False
			# print(self.graph[src], parent)
			if parent in self.graph[src]:
				self.count += 1
				return
			return

		for dest in self.graph[src]:
			# print(src, dest)
			if not visited[dest]:
				# print(dest, parent, n - 1, visited)
				self.DFS(dest, parent, n - 1, visited)

		visited[src] = False


graph = CycleOfLengthN()

edges = [(0, 1), (0, 3), (1, 2), (2, 3), (1, 4), (4, 3)]

for src, dest in edges:

	graph.addEdge(src, dest)

n = 4

print('Cycle of length {} is {}'.format(n, graph.countCycles(0, n)))
