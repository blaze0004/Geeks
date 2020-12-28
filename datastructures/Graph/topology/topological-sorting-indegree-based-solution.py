
# Kahn's algorithm

from collections import defaultdict

class IndegreeKahnTopology:

	def __init__(self, vertices):

		self.graph = defaultdict(list)

		self.V = vertices

		self.indegree = [0] * (self.V)

	def addEdge(self, src, dest):

		self.indegree[dest] += 1

		self.graph[src].append(dest)

	def findTopology(self):

		queue = []

		for i in range(self.V):

			if self.indegree[i] == 0:
				queue.append(i)

		result = []
		cnt = 0
		while queue:

			v = queue.pop(0)
			result.append(v)
			for dest in self.graph[v]:

				if self.indegree != 0:

					self.indegree[dest] -= 1
					if self.indegree[dest] == 0:
						queue.append(dest)
			cnt += 1

		if cnt != self.V:

			print('no topology sort available');

		else:
			print(result)
g = IndegreeKahnTopology(6)
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 

g.findTopology();
