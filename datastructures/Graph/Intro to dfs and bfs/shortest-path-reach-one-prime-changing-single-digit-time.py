
from collections import defaultdict 

class Graph:

	def __init__(self):
		self.vertices = 0
		self.graph = defaultdict(list)

	def addEdge(self, src, dest):

		if not self.graph[src]:
			self.vertices += 1
		if not self.graph[dest]:
			self.vertices += 1

		self.graph[src].append(dest)
		self.graph[dest].append(src)


	def findShortestPath(self, num1, num2):

		primes = self.sieveOfEtheroes()

		for i in primes:
			for j in primes:

				if self.compare(i, j):
					self.addEdge(i, j)

		visited = [False] * 9999
		#print(len(visited))

		visited[num1] = True

		queue = [num1]
		levels = [0] * 9999
		levels[num1] = 0
		while queue:

			np = queue.pop(0)

			for v in self.graph[np]:
			
				if not visited[v]:
					visited[v] = True
					levels[v] = levels[np] + 1
					queue.append(v)
				if v == num2:
					return levels[v] 
			

	def sieveOfEtheroes(self):
		n = 9999
		primes = [True] * (n+1)

		p = 2

		while p*p <= n:

			if primes[p]:

				for i in range(p*2, n+1, p):
					primes[i] = False
			#print('while')

			p += 1

		prime = []

		for i in range(1000, n+1):

			if primes[i]:
				prime.append(i)

		
		return prime

	def compare(self, num1, num2):

		num1 = str(num1)
		num2 = str(num2)

		count = 0

		for i in range(4):
			if num1[i] != num2[i]:
				count += 1

		return count == 1

graph = Graph()

num1 = int(input())
num2 = int(input())

path = graph.findShortestPath(num1, num2)
print(path)