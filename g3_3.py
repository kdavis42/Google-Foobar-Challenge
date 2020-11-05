def solution(l):
	d = {}
	for tup in enumerate(l):
		d[tup] = []

	for key in d:
		for pair in enumerate(l):
			if key[0] < pair[0] and pair[1] % key[1] == 0:
				d[key].append(pair)
	count = 0
	print(d)
	for key in d:
		for child in d[key]:
			count += len(d[child])

	return count


if __name__ == '__main__':
	lst = [1, 2, 3, 4, 5, 6]
	print(solution(lst))
	lst = [1, 1, 1]
	print(solution(lst))