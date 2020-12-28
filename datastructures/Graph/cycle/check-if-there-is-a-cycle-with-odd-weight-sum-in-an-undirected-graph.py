
from collections import defaultdict

class WeightedUndirectedGraph:

	def __init__(self):

		self.graph = defaultdict(dict)
		self.V = 0
		self.E = 0

	def addEdge(self, src, dest, weight):

		if src not in self.graph.keys():
			self.V += 1
		if dest not in self.graph.keys():
			self.V += 1

		self.graph[src].update({dest:weight})
		self.graph[dest].update({src:weight})

		

		self.E += 1

	def removeEdge(self, src, dest):

		self.graph[src].pop(dest)
		self.graph[dest].pop(src)

		if not len(self.graph[src]):
			self.V -= 1

		if not len(self.graph[dest]):
			self.V -= 1

		self.E -= 1

	def printGraph(self):

		for k,v in self.graph.items():
			print(k, ' - ', v)
		print('Keys ' , self.V, ', edges: ' , self.E)
		print('-----')

	def isOddWeight(self, start):
		visited = {key: False for key, _ in self.graph.items()}
		# self.printGraph()
		self.DFS(start, visited)
		# self.printGraph()
		# print(start)
		if self.isBipartite(start):
			return True
		else:
			return False

	def DFS(self, src, visited):

		visited[src] = True
		sourceNeighbours = self.graph[src].copy()
		for dest in sourceNeighbours:

			if not visited[dest]:

				if self.graph[src][dest] % 2 == 0:
					
					pseudo = self.V + 1
					self.removeEdge(src, dest)
					self.addEdge(src, pseudo, 1)
					self.addEdge(pseudo, dest, 1)
					visited[pseudo] = True

				elif self.graph[src][dest] % 2 == 1:
					
					self.graph[src][dest] = 1

				self.DFS(dest, visited)

		visited[src] = False

	def isCycleUtil(self, src, parent, visited, color):

		visited[src] = True

		# print(src, parent)

		# if src == parent and color[src-1] != color[parent-1]:
		# 	return True

		for dest in self.graph[src]:

			if not visited[dest]:
				# print(dest)
				# print(color)
				if not color[dest-1]:

					color[dest-1] = 1 - color[src-1]
					# print(color[dest-1], color[src-1])

					if self.isCycleUtil(dest, parent, visited, color):
						return True
			
			elif dest == parent and color[dest -1] == color[src-1]:
				return True
			# print(src, dest, parent, color[dest-1], color[parent-1])
		visited[src] = False
		return False
		


	def isBipartite(self, start):

		visited = {key: False for key, _ in self.graph.items()}
		# print(visited)
		
		color   = [0] * (self.V)
		# print(color)

		for i in self.graph.keys():

			if not visited[i]:

				if self.isCycleUtil(i, i, visited, color):
					return True

		return False




graph = WeightedUndirectedGraph()

edges = [(1, 2, 12), (2, 3, 1), (4, 3, 1), (4, 1, 21)]
# edges = [(1, 2, 2), (1, 5, 2), (5, 2, 2), (1, 4, 2), (2, 6, 2), (2, 3, 2), (6, 4, 2), (4, 3, 2)]
# print(len(edges))
for src, dest, weight in edges:

	graph.addEdge(src, dest, weight)

print(graph.isOddWeight(1))
