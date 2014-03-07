# Solution to exercise MinAvgTwoSlice
# http://www.codility.com/train/

def solution(A):
	
    # The minimal average slice will be either of length 2 or length 3
	
    N = len(A)
    min_average = 3*(A[0] + A[1])
    start_location = 0
    for i in range(N-1):
        if 3*(A[i] + A[i+1]) < min_average:
            min_average = 3*(A[i] + A[i+1])
            start_location = i
	
    for i in range(N-2):
        if 2*(A[i] + A[i+1] + A[i+2]) < min_average:
            min_average = 2*(A[i] + A[i+1] + A[i+2])
            start_location = i

    return start_location