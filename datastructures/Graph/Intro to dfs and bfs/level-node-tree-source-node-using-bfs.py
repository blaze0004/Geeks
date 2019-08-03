
from collections import defaultdict

class Graph:

	def __init__(self):
		self.V = 0
		self.graph = defaultdict(list)

	def addEdge(self, src, dest):
		if src not in self.graph:
			self.V += 1
		if dest not in self.graph:
			self.V += 1

		self.graph[src].append(dest)
		self.graph[dest].append(src)

	def levelOfEachNode(self, src):
		# print(self.V)
		visited = [0] * (self.V)

		queue = [src]

		visited[src] += 1

		while queue:

			s = queue.pop(0)

			for i in self.graph[s]:
				# print(i)
				if not visited[i]:
					visited[i] = visited[s] + 1
					queue.append(i)


		return map(lambda x: x-1, visited)

	def printNodeLevel(self, src):

		print('Node\tLevel')
		n = 0
		for i in self.levelOfEachNode(src):

			print('{}\t\t{}'.format(n, i))
			n += 1

graph = Graph()
# graph[0].push_back(1); 
#     graph[0].push_back(2); 
#     graph[1].push_back(3); 
#     graph[1].push_back(4); 
#     graph[1].push_back(5); 
#     graph[2].push_back(5); 
#     graph[2].push_back(6); 
#     graph[6].push_back(7); 
graph.addEdge(0, 1)
graph.addEdge(0, 2)
graph.addEdge(1, 3)
graph.addEdge(1, 4)
graph.addEdge(1, 5)
graph.addEdge(2, 5)
graph.addEdge(2, 6)
graph.addEdge(6, 7)
graph.printNodeLevel(0)
