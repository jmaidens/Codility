# Solution to exercise FrogRiverOne
# http://www.codility.com/train/

def solution(X, A):
    
    count_array = [0 for i in range(X+1)]
    empty_positions = X
    
    for i in range(len(A)):
        a = A[i]
        if count_array[a] == 0:
            empty_positions -= 1
        count_array[a] += 1
        if empty_positions == 0:
            return i
	
    return -1