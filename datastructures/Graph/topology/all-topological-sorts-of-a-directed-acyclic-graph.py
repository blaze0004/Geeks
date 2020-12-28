
from collections import defaultdict

class AllTopologicalSorts:
	"""docstring for AllTopologicalSorts"""
	def __init__(self, vertices):
		super(AllTopologicalSorts, self).__init__()
		
		self.graph = defaultdict(list)
		self.V = vertices
		self.indegree = [0] * (self.V)

	def addEdge(self, src, dest):
		
		self.indegree[dest] += 1
		self.graph[src].append(dest)


	def printAllSorts(self):

		visited = [False] * (self.V)
		result = []

		self.printAllSortsUtils( result, visited);

	def printAllSortsUtils(self, result, visited):

		flag = False

		for i in range(self.V):

			if self.indegree[i] == 0 and not visited[i]:

				for dest in self.graph[i]:

					self.indegree[dest] -= 1

				result.append(i)
				visited[i] = True
				self.printAllSortsUtils(result, visited)

				visited[i] = False
				result.pop()

				for dest in self.graph[i]:

					self.indegree[dest] += 1

				flag = True

		if not flag:

			for i in result:
				print(i, end = ' ')

			print('')



g = AllTopologicalSorts(6)
g.addEdge(5, 2); 
g.addEdge(5, 0); 
g.addEdge(4, 0); 
g.addEdge(4, 1); 
g.addEdge(2, 3); 
g.addEdge(3, 1); 

g.printAllSorts()