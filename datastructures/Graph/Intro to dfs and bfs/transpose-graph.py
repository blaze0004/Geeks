
from collections import defaultdict


class Graph:

	def __init__(self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)

	def addEdge(self, src, dest):

		self.graph[src].append(dest)

	def transposeGraph(self):

		transpose = Graph(self.V)

		for k, v in self.graph.items():

			for i in v:

				transpose.addEdge(i, k)

		return transpose

def printGraph(graph):

		print('Graph is: ')

		for k, v in graph.items():
			print('{} -> {}'.format(k, v))
		print('.....')

graph = Graph(6)

graph.addEdge( 0, 1); 
graph.addEdge( 0, 4); 
graph.addEdge( 0, 3); 
graph.addEdge( 2, 0); 
graph.addEdge( 3, 2); 
graph.addEdge( 4, 1); 
graph.addEdge( 4, 3);

printGraph(graph.graph)

transpose = graph.transposeGraph()

printGraph(transpose.graph)