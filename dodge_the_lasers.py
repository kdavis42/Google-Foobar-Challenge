def lasers(s):

	return str(beatty(sqrt(2), int(s)))

def floor(num):
	return int(num)

def beatty(alpha, n):

	#if n >= 2:
		#return (n*(n+1))/2 + s(alpha - 1, n)
	if n >= 1:
		m = floor(n*(alpha-1))
		leftSide = n*m + n*(n+1)/2 - m*(m+1)/2
		return leftSide - beatty(alpha, m)
	else:
		return 0

def sqrt(num):
	return num ** .5

if __name__ == '__main__':
	print(lasers('5'))
	print(lasers('77'))
	
	#print(s(sqrt(2), 2))