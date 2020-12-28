

class JugFilling:

	def __init__(self, jug1, jug2, target):

		self.firstJugCapacity = jug1
		self.secondJugCapacity = jug2
		self.target = target

	def BFSMethod(self):

		visited = {}
		path = []
		isSolvable = False
		queue = [(0, 0)]

		while queue:

			state = queue.pop(0)
			try:
				if visited[state]:
					continue
			except KeyError:
				visited[state] = False

			if state[0] > self.firstJugCapacity or state[1] > self.secondJugCapacity or state[0] < 0 or state[1] < 0:
				continue

			visited[state] = True
			path.append(state)

			if state[0] == self.target or state[1] == self.target:

				isSolvable = True

				if state[0] == self.target and state[1] != 0:
					path.append((state[0], 0))
				elif state[1]== self.target and state[0] != 0:
					path.append((0, state[1]))

				for i in path:
					print(i, end=' ')
				print('')

			queue.append((self.firstJugCapacity, state[1]))
			queue.append((state[0], self.secondJugCapacity))

			for ap in range(0, max(self.firstJugCapacity, self.secondJugCapacity)+1):

				c = state[0] + ap;
				d = state[1] - ap;

				if c == self.firstJugCapacity or (d == 0 and d >= 0):
					queue.append((c, d))

				c = state[0] - ap;
				d = state[1] + ap;

				if (c == 0 and c >= 0) or d == self.secondJugCapacity:

					queue.append((c, d))

			queue.append((self.firstJugCapacity, 0))
			queue.append((0, self.secondJugCapacity))


		if not isSolvable:
			print('Not Solvable')





	def DFSMethod(self):
		pass


jugs = JugFilling(4, 3, 2)
jugs.BFSMethod()