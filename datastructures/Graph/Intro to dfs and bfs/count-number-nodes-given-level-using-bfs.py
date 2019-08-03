

from collections import defaultdict

class Graph:

	def __init__(self, vertices):

		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self, src, dest):

		self.graph[src].append(dest)
		self.graph[dest].append(src)

	def countNodeAtGivenLevel(self, root, level):

		visited = [False]*self.V
		levels = [0]* self.V

		queue = [root]
		visited[root] = True

		while queue:

			v = queue.pop(0)

			for i in self.graph[v]:

				if not visited[i]:
					levels[i] += levels[v] + 1
					visited[i] = True
					queue.append(i)

		count = 0

		print(levels)

		for i in levels:
			if i == level:
				count += 1

		return count

g = Graph(6)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)

level = 2

print('Number of nodes at level {} is {}'.format(level, g.countNodeAtGivenLevel(0, level)))