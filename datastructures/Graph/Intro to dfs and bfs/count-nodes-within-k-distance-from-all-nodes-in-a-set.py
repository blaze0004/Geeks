
from Graph import UnDirectedGraph

class KDistance(UnDirectedGraph):

	def __init__(self):
		UnDirectedGraph.__init__(self)

	def countNodesAtKDistFromMarked(self, marked, k):

		prevVisited = [0] * (self.V)
		#self.BFS(marked, i, k, visited)
		visited = []
		for mark in marked:

			visited = [0] * self.V

			visited[mark] += 0
			

			queue = [mark]

			while queue:

				v = queue.pop(0)

				# if prevVisited[v] and prevVisited[v] > k:
				# 	visited[v] = prevVisited[v]

				for i in self.graph[v]:

					if not visited[i]:

						visited[i] += visited[v] + 1

						queue.append(i)

					# if visited[i] > k:
					# 	visited[i] = prevVisited[i]
				# if visited[v] > k:
				# 	visited[v] = prevVisited[v]
			prevVisited = visited

		for i in map(lambda x: x, visited):
			print(i, end = ' ')

	def BFS(self, marked, i, k, visited):

		src = marked[i]
		visited[src] += 1

		queue = [src]

		while queue:

			s = queue.pop(0)

			if visited[s] > k:
				break

			visited[s] = 0

			for v in self.graph[s]:

				if not visited[v]:

					visited[v] = visited[s] + 1
					queue.append(v)

		self.BFS(marked, i+1, k, visited)

graph = KDistance()

graph.addEdge(1, 0)
graph.addEdge(0, 3)
graph.addEdge(0, 8)
graph.addEdge(2, 3)
graph.addEdge(3, 5)
graph.addEdge(3, 6)
graph.addEdge(3, 7)
graph.addEdge(4, 5)
graph.addEdge(5, 9)

marked = [1,2, 4]
k = 3
graph.countNodesAtKDistFromMarked(marked, k)

# [1, 0, 3, 2, 4, 3, 3, 3, 2, 4]
# [2, 3, 0, 1, 4, 2, 2, 2, 3, 4] [3, 3, 3, 3, 8, 5, 5, 5, 5, 8]
# [3, 4, 3, 2, 4, 1, 3, 3, 4, 4] [6, 7, 6, 5, 12, 6, 8, 8, 9, 12] [3, 4, 3, 2, 9, 3, 5, 5, 6, 9]
