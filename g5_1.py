from collections import Counter

def factorialDP(n):
	mem = [1]
	for num in range(1, n+1):
		mem.append(num*mem[-1])
	return mem

def factorial(n, mem):
	return mem[n]

def gcd(num0, num1):
	def absGCD(num0, num1):
		if num1 == 0:
			return num0
		return absGCD(num1, num0 % num1)
	return absGCD(abs(num0), abs(num1))

def cycle_count(c, n, mem):
	count = factorial(n, mem)
	for a, b in Counter(c).items():
		count//=(a**b)*factorial(b, mem)
	return count

def cycle_partition(n, i=1):
	lst = [[n]]
	for k in range(i, n/2 + 1): #n//2
		for part in cycle_partition(n - k, k):
			lst.append([k] + part)
	return lst

def answer(w, h, s):
	grid = 0
	mem = factorialDP(max(w, h))
	for partH in cycle_partition(h):
		for partW in cycle_partition(w):
			m = cycle_count(partW, w, mem)*cycle_count(partH, h, mem)
			exp = sum([sum([gcd(i, j) for i in partW]) for j in partH])
			grid += m*(s**exp)
	repW = factorial(w, mem)
	repH = factorial(h, mem)
	return str(grid//(repW * repH))

if __name__ == '__main__':

	print(answer(2, 2, 2))
	print(answer(2, 3, 4))
	#permutations = list(itertools.product([0, 1], repeat=4))
	#print(len(permutations))








