
from collections import defaultdict
import heapq
from sys import maxsize
class MSTPrimsAdj:

	def __init__(self, vertices):

		self.graph = defaultdict(dict)
		self.V = vertices

	def addEdge(self, src, dest, weight):

		self.graph[src].update({dest:weight})

	def findMST(self, src):

		heap = []
		dist = [maxsize] * (self.V)
		visited = [False] * (self.V)
		visited[src] = 0
		dist[src] = 0
		result = []

		heapq.heappush(heap, (dist[0], src, -1))

		while heap:

			weight, current, parent = heapq.heappop(heap)
			
			result.append((parent, current))
			for d, w in self.graph[current].items():

				if not visited[d]:

					if dist[d] != maxsize and dist[d] > dist[current] + w:

						dist[d] = dist[current] + w


					heapq.heappush(heap, (dist[d], d, current))
					visited[d] = True
		s = 0
		for parent, dest in result[1:]:
			print(parent, ' - ', dest, dist[dest])
			s += dist[dest]
		print(s)

graph = MSTPrimsAdj(9) 
graph.addEdge(0, 1, 4) 
graph.addEdge(0, 7, 8) 
graph.addEdge(1, 2, 8) 
graph.addEdge(1, 7, 11) 
graph.addEdge(2, 3, 7) 
graph.addEdge(2, 8, 2) 
graph.addEdge(2, 5, 4) 
graph.addEdge(3, 4, 9) 
graph.addEdge(3, 5, 14) 
graph.addEdge(4, 5, 10) 
graph.addEdge(5, 6, 2) 
graph.addEdge(6, 7, 1) 
graph.addEdge(6, 8, 6) 
graph.addEdge(7, 8, 7) 
graph.findMST(0) 