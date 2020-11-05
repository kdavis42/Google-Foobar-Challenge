from __future__ import division

def solution(pegs):
	invalidGear = [-1, -1]
	N = len(pegs)
	constraints = []

	#finding distances between pegs
	for i in range(N-1):
		constraints.append(pegs[i+1]-pegs[i])

	#radius of first peg found by adding even indexed values in constraints
	#and subtracting odd indexed values and multiplying result by 2
	#if number of pegs is even divisor is 3 else 1

	r_0 = 0
	sign = 1

	for val in constraints:
		r_0 += (sign * val)
		sign *= -1

	r_0 *= 2

	if N % 2 == 0:
		divisor = 3
	else:
		divisor = 1

	if r_0 % divisor == 0:
		r_0 /= divisor
		divisor = 1

	#first radius must be > 2 since last radius is (first radius)/2 and all radii >= 1
	if r_0 < 2:
		return invalidGear

	testRadius = r_0 / divisor
	for i in range(len(constraints) - 1):
		if testRadius < 1 or testRadius > constraints[i] - 1:
			return invalidGear
		testRadius = constraints[i] - testRadius

	return [r_0, divisorß]