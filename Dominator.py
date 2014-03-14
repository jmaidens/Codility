def solution(A):
    N = len(A)
    
    # Remove two elements of array with different values until
    # all elements in array have same value
    size = 0
    for i in range(N):
        if size == 0:
            value = A[i]
            size = 1
        else:
            if value == A[i]:
                size += 1
            else:
                size -= 1
	
	# Check that the remaining value is indeed a dominator
	
    candidate = -1
    if size > 0:
        candidate = value
	
    count = 0
    for i in range(N):
        if A[i] == candidate:
            count += 1
	
    if count > N/2:
        i = 0
        while A[i] != candidate:
            i += 1
        return i
    else:
        return -1


