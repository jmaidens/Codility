# Solution to exercise TapeEquilibrium
# http://www.codility.com/train/

def solution(A):
	
	N = len(A)
	
	# Create array of prefix sums
	prefix_sums = [A[0]]
	for i in range(N-1):
		prefix_sums.append(prefix_sums[i] + A[i+1])

	# Iterate though all differences, keeping the smallest
	# Each difference can be evaluated in time O(1)
	min_difference = abs(prefix_sums[N-1] - 2*prefix_sums[0])
	for i in range(N-1):
		min_difference = min(min_difference,
							 abs(prefix_sums[N-1] - 2*prefix_sums[i]))

	return min_difference

