
from collections import defaultdict
import sys
class DetectNegativeCycle:
	"""docstring for DetectNegativeCycle"""
	def __init__(self):

		self.V = 0
		self.graph = defaultdict(dict)

	def addEdge(self, src, dest, weight):

		self.graph[src].update({dest:weight})
		self.V += 1


	def isNegativeCycle(self, start):
		
		dist = [sys.maxsize] * (self.V)
		dist[start] = 0
		for i in range(self.V - 1):

			for src in self.graph.keys():
				for neighbour in self.graph[src]:
					weight = self.graph[src][neighbour]
					# print(src, neighbour, weight, end = ', ')
					# print(dist[src])
					if dist[src] != sys.maxsize and (dist[src] + weight) < dist[neighbour]:
						dist[neighbour] = dist[src] + weight
						# print('dfsh')
				# print(' ')
		# print(dist)
		for src in self.graph.keys():
			for neighbour in self.graph[src]:
				weight = self.graph[src][neighbour]

				if dist[src] != sys.maxsize and (dist[src] + weight) < dist[neighbour]:
					return True
		return False



graph = DetectNegativeCycle()

edges = [(0, 1, 1), (1, 2, -1), (2, 3, -1), (3, 0, -1)]


edges2 = [(1, 2, 4), (6, 2, 3), (1, 3, 4), (4, 1, 3),
		  (4, 3, 2), (7, 6, 2),
		 (3, 6, -2), (3, 5, 4), (5, 4, 1), (6, 5, -3),
		 (5, 7, -2), (7, 8, 2), (8, 5, -2)]

for src, dest, weight in edges:

	graph.addEdge(src, dest, weight)

print(graph.isNegativeCycle(1))

