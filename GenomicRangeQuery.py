# Solution to exercise GenomicRangeQuery
# http://www.codility.com/train/

def solution(S, P, Q):
	N = len(S)
	
	# Create arrays of the number of times each nucleotide N appears
	# N[i] is the number of times N appears up to positon i
	A = [0]
	C = [0]
	G = [0]
	T = [0]
	for i in range(0, N):
		A.append(A[-1])
		C.append(C[-1])
		G.append(G[-1])
		T.append(T[-1])
		if S[i] == 'A':
			A[-1] += 1
		elif S[i] == 'C':
			C[-1] += 1
		elif S[i] == 'G':
			G[-1] += 1
		elif S[i] == 'T':
			T[-1] += 1

	# Compute the minimal nucleotide in the range (P[i], Q[i])
	ans = []
	for i in range(len(P)):
		if A[Q[i]+1] - A[P[i]] > 0:
			ans.append(1)
		elif C[Q[i]+1] - C[P[i]] > 0:
			ans.append(2)
		elif G[Q[i]+1] - G[P[i]] > 0:
			ans.append(3)
		elif T[Q[i]+1] - T[P[i]] > 0:
			ans.append(4)
	return ans

