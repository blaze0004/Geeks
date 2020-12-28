
from Graph import DirectedGraph
from collections import defaultdict
import queue

class BestFirstSearchGraph(DirectedGraph):

	def __init__(self, root = 0):

		DirectedGraph.__init__(self)
		self.graph = defaultdict(dict)
		self.root = root

	def addEdge(self, src, dest, weight):

		self.graph[src].update({dest:weight})
		self.graph[dest].update({src: weight})
		self.V += 2

	def doBestFirstSearch(self, dest):
		# print(self.graph['s'])

		visited = {key:False for key in self.graph.keys()}
		s = list(self.graph[self.root].keys())[0]
		pqueue = queue.PriorityQueue()
		pqueue.put((0, self.root))
		visited[self.root] = True
		# path = []	
		while pqueue.qsize():

			minV = pqueue.get()[1]
			#print(minV)
			# path.append(minV)
			if minV == dest:
				print(path)
				return True
			# print(minV)
			# print(self.graph[minV])
			for k,v  in self.graph[minV].items():
			
				if not visited[k]:

					# path.append(k)
					visited[k] = True

					pqueue.put((v, k))


		return False


graph = BestFirstSearchGraph(root = 's')

graph.addEdge('s', 'a', 3)
graph.addEdge('a', 'd', 9)
graph.addEdge('a', 'e', 8)
graph.addEdge('s', 'b', 6)
graph.addEdge('b', 'f', 12)
graph.addEdge('b', 'g', 14)
graph.addEdge('s', 'c', 5)
graph.addEdge('c', 'h', 7)
graph.addEdge('h', 'i', 5)
graph.addEdge('i', 'k', 1)
graph.addEdge('i', 'l', 10)
graph.addEdge('i', 'm', 2)
graph.addEdge('h', 'j', 6)

print(graph.doBestFirstSearch('i'))