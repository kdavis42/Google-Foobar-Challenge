def solution(num_buns, num_required):
	#first if handles test 5
	#if and elif part solve tests 1, 2, 6
	if num_required == 0:
		return [[]]
	if num_required == 1:
		return [[0] for _ in range(num_buns)]
	elif num_buns == num_required:
		return [[i] for _ in range(num_buns)]
	else:
		num_keys = choose(num_buns, num_required)
		#keys = [i for i in range(num_keys)]

		key_distr = [[] for _ in range(num_buns)]
		curKey = 0
		for bunnyCombo in combosOf(key_distr, num_buns-num_required+1):
			for bunny in bunnyCombo:
				bunny.append(curKey)
			curKey+=1
		return key_distr


def combosOf(iterable, n):
	#all combinations of subsets of iterable of length n
	if n == 0:
		return [[]]
	combos = []
	for i in range(len(iterable)):
		first = iterable[i]
		for rest in combosOf(iterable[i+1:], n-1):
			combos.append([first] + rest)
	return combos
def choose(n, k):
	denominator = 1
	numerator = 1
	for i in range(2, n+1):
		numerator *= i
		if i == k or i == (n-k):
			denominator *= numerator
	return numerator/denominator


if __name__ == '__main__':
	#print(combosOf(['A', 'B', 'C'], 2))
	print(solution(5, 3))
