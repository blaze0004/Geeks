
from collections import defaultdict

class MaximumEdgesDag:

	def __init__(self, vertices):

		self.graph = defaultdict(list)
		self.V = vertices

	def addEdge(self, src, dest):

		self.graph[src].append(dest)

	def findMaxEdges(self):

		indegree = [0] * (self.V)

		queue = []
		topologySort = []
		cnt = 0

		for src in self.graph:

			for dest in self.graph[src]:

				indegree[dest] += 1


		for i in range(self.V):

			if indegree[i] == 0: queue.append(i)


		while queue:

			v = queue.pop(0)
			topologySort.append(v)

			for i in self.graph[v]:

				indegree[i] -= 1

				if indegree[i] == 0:
					queue.append(i)

			cnt += 1
		if cnt != self.V:
			return False
		else:
			result = []
			for src in range(cnt):

				for dest in range(src, cnt):

					if src != dest:
						if topologySort[dest] not in self.graph[topologySort[src]]:

							result.append((topologySort[src], topologySort[dest]))
							self.graph[topologySort[src]].append(topologySort[dest])

			print('Total number of max edges added are: ', len(result))
			for src, dest in result:
				print('{}-{}'.format(src, dest), end = ', ')
			print('\B')	




g = MaximumEdgesDag(6)
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 

g.findMaxEdges();