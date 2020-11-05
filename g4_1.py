def solution(entrances, exits, paths):

	numOfRooms = len(path)
	intermediateRooms = [x for x in range(numOfRooms) if not x in entrances and not x in exits]
	flow = 0
	for interNode in intermediateRooms:
		maxExitFlow = sum(path[interNode])
		maxEnterFlow = sum([path[entrance][interNode] for entrance in entrances])
		flow += min(maxEnterFlow, maxExitFlow)

	return flow
if __name__ == '__main__':
	entrances = [0]
	exits = [3]
	paths = [
		[0, 7, 0, 0],
		[0, 0, 6, 0],
		[0, 0, 0, 8],
		[9, 0, 0, 0]
	]

	print(solution(entrances, exits, paths))

	entrances = [0, 1]
	exits = [4, 5]
	paths = [
		[0, 0, 4, 6, 0, 0],
		[0, 0, 5, 2, 0, 0],
		[0, 0, 0, 0, 4, 4],
		[0, 0, 0, 0, 6, 6],
		[0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0]
	]

	print(solution(entrances, exits, paths))








