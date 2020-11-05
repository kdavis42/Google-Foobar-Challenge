def solution(n):

	n = int(n)
	count = 0

	while n != 1:
		if n & 1 == 0:
			n >>= 1
		elif n == 3 or (n & 0b11) == 0b01:#(n & 1 and (n >> 1 & 1) == 1):
			n -= 1
		else:
			n += 1
		count += 1

	return count

if __name__ == '__main__':
	
	print(solution('4'))
	print(solution('15'))




