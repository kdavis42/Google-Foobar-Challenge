def solution(m):
	# get a matrix at most 10x10
	N = len(m)

	terminalStates = []
	
	if N == 1:
	    return [1, 1]

	for row in range(N):
		if not any(m[row]):
			terminalStates.append(row)
	
	#if all states are terminal then will always end up in state 0
	if len(terminalStates) == N:
	    res = []
	    for i in range(N):
	        if i == 0:
	            res.append(1)
	        else:
	            res.append(0)
	    res.append(1)
	    return res

	#probably want to normalize it
	m = normalize(m, N)
	nonTerm = []

	for row in range(N):
		if row in terminalStates:
			continue
		newRow = []
		for col in range(N):
			if col not in terminalStates:
				newRow.append(m[row][col])
		nonTerm.append(newRow)

	smallN = len(nonTerm)
	for row in range(smallN):
		for col in range(smallN):
			if row == col:
				nonTerm[row][col] = oneMinus(nonTerm[row][col])
			else:
				nonTerm[row][col] = (-nonTerm[row][col][0], nonTerm[row][col][1])

	nonTerm = getMatrixInverse(nonTerm)

	R = []
	for col in terminalStates:
		newRow = []
		for row in range(N):
			if row not in terminalStates:
				newRow.append(m[row][col])
		R.append(newRow)
	R = transposeMatrix(R)

	state0Prob = matrixMultiply(nonTerm, R)[0]
	maxDenom = 1
	for fraction in state0Prob:
		maxDenom = max(maxDenom, lcm(maxDenom, fraction[1]))

	result = []
	for fraction in state0Prob:
		denom = fraction[1]
		lcd = lcm(maxDenom, denom)
		result.append(fraction[0]*(lcd/denom))
	result.append(maxDenom)
	
	return result

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDet(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return subFractions(multFractions(m[0][0], m[1][1]), multFractions(m[0][1], m[1][0]))

    determinant = (0, 1)
    for c in range(len(m)):
        determinant = addFractions(determinant, multFractConst(((-1)**c), multFractions(m[0][c], getMatrixDet(getMatrixMinor(m,0,c)))))
    return determinant

def getMatrixInverse(m):
    determinant = getMatrixDet(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
    	a = divFractions(m[1][1], determinant)
    	b = divFractions(multFractConst(-1, m[0][1]), determinant)
    	c = divFractions(multFractConst(-1,m[1][0]), determinant)
    	d = divFractions(m[0][0], determinant)
        return [[a, b],
                [c, d]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(multFractConst(((-1)**(r+c)), getMatrixDet(minor)))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = divFractions(cofactors[r][c], determinant)
    return cofactors

def transposeMatrix(m):
    return map(list,zip(*m))

def subFractions(fract1, fract2):
	numer1 = fract1[0] * fract2[1]
	numer2 = fract2[0] * fract1[1]
	denom = fract1[1] * fract2[1]
	return simplify(numer1 - numer2, denom)

def addFractions(fract1, fract2):
	numer1 = fract1[0] * fract2[1]
	numer2 = fract2[0] * fract1[1]
	denom = fract1[1] * fract2[1]
	return simplify(numer1 + numer2, denom)

def multFractions(fract1, fract2):
    return simplify(fract1[0] * fract2[0], fract1[1] * fract2[1])

def multFractConst(constant, fraction):
    return simplify(fraction[0] * constant, fraction[1])

def divFractions(fract1, fract2):
    return simplify(fract1[0] * fract2[1], fract1[1] * fract2[0])

def divFractConst(fraction, constant):
    return simplify(fraction[0], fraction[1] * constant)

def matrixMultiply(A, B):
	result = [[0 for _ in range(len(B[0]))] for _ in range(len(B))]

	for i in range(len(A)):
		for j in range(len(B[0])):
			val = (0, 1)
			for k in range(len(B)):
				val = addFractions(val, multFractions(A[i][k], B[k][j]))
			result[i][j] = val
	return result

def oneMinus(fract):
	#fraction that is denoted by (numerator, denominator)
	return simplify(fract[1] - fract[0], fract[1])

def normalize(m, N):
	for i in range(N):
		denominator = sum(m[i])
		for j in range(N):
			val = m[i][j]
			divisor = gcd(val, denominator)
			m[i][j] = (val/divisor, denominator/divisor) if divisor else (val, denominator)

	return m

def gcd(num1, num2):
    def gcd1(num1, num2):
        if num2:
            return gcd1(num2, num1 % num2)
        else:
            return num1
    return gcd1(abs(num1), abs(num2))

def lcm(num1, num2):
	return (num1 * num2) / gcd(num1, num2)

def simplify(numerator, denominator):
    div = gcd(numerator, denominator)
    return (numerator/div, denominator/div)

"""assert (
   	solution([
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]) == [7, 6, 8, 21]
)
 
assert (
    solution([
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]) == [0, 3, 2, 9, 14]
)
 
assert (
    solution([
        [1, 2, 3, 0, 0, 0],
        [4, 5, 6, 0, 0, 0],
        [7, 8, 9, 1, 0, 0],
        [0, 0, 0, 0, 1, 2],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]) == [1, 2, 3]
)
assert (
    solution([
        [0]
    ]) == [1, 1]
)
 
assert (
    solution([
        [0, 0, 12, 0, 15, 0, 0, 0, 1, 8],
        [0, 0, 60, 0, 0, 7, 13, 0, 0, 0],
        [0, 15, 0, 8, 7, 0, 0, 1, 9, 0],
        [23, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [37, 35, 0, 0, 0, 0, 3, 21, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [1, 2, 3, 4, 5, 15]
)
 
assert (
    solution([
        [0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
        [0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
        [0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
        [48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
        [0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [4, 5, 5, 4, 2, 20]
)
 
assert (
    solution([
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [1, 1, 1, 1, 1, 5]
)
 
assert (
    solution([
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [2, 1, 1, 1, 1, 6]
)
 
assert (
    solution([
        [0, 86, 61, 189, 0, 18, 12, 33, 66, 39],
        [0, 0, 2, 0, 0, 1, 0, 0, 0, 0],
        [15, 187, 0, 0, 18, 23, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [6, 44, 4, 11, 22, 13, 100]
)
 
assert (
    solution([
        [0, 0, 0, 0, 3, 5, 0, 0, 0, 2],
        [0, 0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 4, 4, 0, 0, 0, 1, 1],
        [13, 0, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 8, 7, 0, 0, 0, 1, 3, 0],
        [1, 7, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]) == [1, 1, 1, 2, 5]
)"""

if __name__ == '__main__':
	matrix = [
		[0, 7, 0, 17, 0, 1, 0, 5, 0, 2],
		[0, 0, 29, 0, 28, 0, 3, 0, 16, 0],
		[0, 3, 0, 0, 0, 1, 0, 0, 0, 0],
		[48, 0, 3, 0, 0, 0, 17, 0, 0, 0],
		[0, 6, 0, 0, 0, 1, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	]
	answer = solution(matrix)
	print(answer)