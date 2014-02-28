# Solution to exercise MaxProductOfThree
# http://www.codility.com/train/

def solution(A):
	# Maximum product will be of the mamimal element with either the two largest or two smallest elements. These could be found in time O(N), but since this problem is about sorting, we do it in time O(N log N) using sort(). 
    A.sort()
    N = len(A)
    return max(A[N-1]*A[0]*A[1], A[N-1]*A[N-2]*A[N-3])
