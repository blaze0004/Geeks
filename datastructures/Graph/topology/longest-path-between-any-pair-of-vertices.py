# longest-path-between-any-pair-of-vertices

from Graph import DirectedGraph
from collections import defaultdict
import sys

class LongestPath(DirectedGraph):

	def __init__(self, vertices):

		DirectedGraph.__init__(self)
		self.graph = defaultdict(dict)
		self.V = vertices

	def addEdge(self, src, dest, weight):

		self.graph[src].update({dest:weight})

	def findMaxPath(self):

		dist = [-sys.maxsize] * (self.V)

		indegree = [0] * (self.V)

		queue = []
		topology = []
		cnt = 0

		for src in self.graph:
			for dest in self.graph[src].keys():

				indegree[dest] += 1

		for i in range(self.V):

			if indegree[i] == 0: queue.append(i)

		dist[queue[0]] = 0
		while queue:

			v = queue.pop(0)
			topology.append(v)

			for dest in self.graph[v].keys():
				if indegree[dest] > 0:
					indegree[dest] -= 1
					if indegree[dest] == 0: queue.append(dest)

			cnt += 1

		if cnt != self.V:
			print('Not a DaG, can\'t find')
		else:

			for src in topology:

				if dist[src] != sys.maxsize:

					for dest, weight in self.graph[src].items():

						if dist[dest] < dist[src] + weight:
							dist[dest] = dist[src] + weight

		print(dist)

edges = [(1, 2, 3), (2, 3, 4), (2, 6, 2), (6, 4, 6), (6, 5, 5)]
n = 6

g = LongestPath(6)

for src,dest,weight in edges:
	g.addEdge(src-1, dest-1, weight)

g.findMaxPath()