# Solution to exercise Triangle
# http://www.codility.com/train/

def solution(A):
	
    # Uses the fact that an ordered list A contains a triangular triplet if and only if it contains a triangular triplet consisting of three consecutive entries
    A.sort()
    
    for i in range(len(A) - 2):
        P = A[i]
        Q = A[i+1]
        R = A[i+2]
        if P + Q > R and Q + R > P and R + P > Q:
            return 1
	
    return 0