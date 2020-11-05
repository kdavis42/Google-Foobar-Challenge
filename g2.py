def solution(n, b):
	visited = {}
	timeStamp = 0
	curID = n
	while not isConstant(curID, b):

		visited[curID] = timeStamp
		timeStamp += 1

		nextID = getNextID(curID, b)

		if nextID in visited:
			return visited[curID] - visited[nextID] + 1
		else:
			curID = nextID

	return 1


def getNextID(n, b):
	"""Takes in string n and int b and returns string of next ID"""
	k = len(n)

	curIDArr = sorted(n)

	x = ''.join(reversed(curIDArr))
	y = ''.join(curIDArr)

	x = int(x, b)
	y = int(y, b)
	zBase10 = x - y

	z = ''
	while zBase10 != 0:
		r = str(zBase10 % b)
		zBase10 /= b
		z = ''.join([r, z])

	while len(z) != k:
		z = ''.join(['0', z])
	return z


def isConstant(id, b):
	return id == getNextID(id, b)

	


if __name__ == '__main__':
	print("number of steps in cycle: " + str(solution('0', 10)))

