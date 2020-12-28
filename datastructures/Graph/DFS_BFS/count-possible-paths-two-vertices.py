
from collections import defaultdict


class Graph:

	def __init__(self, vertices):

		self.V = vertices
		self.graph = defaultdict(list)
		self.path = 0

	def addEdge(self, src, dest):

		self.graph[src].append(dest)

	def countPathUtil(self, src, dest):

		visited = [False]*self.V
		visited[src] = True
		self.countPath(src, dest, visited)

		print('Number of possible path between {} and {} is {}'.format(src, dest, self.path))
		self.path = 0


	def countPath(self, src, dest, visited):

		if src == dest:
			self.path += 1

		else:

			for i in self.graph[src]:

				if not visited[i]:
					visited[i] = True

					self.countPath(i, dest, visited)
		visited[src] = False


graph = Graph(6) 
graph.addEdge(0, 1);
graph.addEdge(0, 2);
graph.addEdge(1, 2);
graph.addEdge(1, 3);
graph.addEdge(3, 4);
graph.addEdge(2, 3);
graph.addEdge(4, 5);

s = 0
d = 5
graph.countPathUtil(s, d)