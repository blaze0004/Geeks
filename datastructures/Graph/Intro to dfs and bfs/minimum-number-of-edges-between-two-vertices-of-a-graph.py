
from collections import defaultdict
from Graph import UnDirectedGraph
class MinEdgeGraph(UnDirectedGraph):

	def __init__(self):
		UnDirectedGraph.__init__(self);

	def findMinEdge(self, src, dest):

		visited = [0] * (self.V)

		queue = [src]

		while queue:

			s = queue.pop(0)

			for i in self.graph[s]:

				if not visited[i]:

					visited[i] = visited[s] + 1

					queue.append(i)

		return visited[dest]

graph = MinEdgeGraph()

graph.addEdge( 0, 1); 
graph.addEdge( 0, 7); 
graph.addEdge( 1, 7); 
graph.addEdge( 1, 2); 
graph.addEdge( 2, 3); 
graph.addEdge( 2, 5); 
graph.addEdge( 2, 8); 
graph.addEdge( 3, 4); 
graph.addEdge( 3, 5); 
graph.addEdge( 4, 5); 
graph.addEdge( 5, 6); 
graph.addEdge( 6, 7); 
graph.addEdge( 7, 8);

#graph.printGraph()
print(graph.findMinEdge(0, 5))