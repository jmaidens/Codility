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
	
	
	# Count the total number of times that the remaining value occurs
    candidate = -1
    if size > 0:
        candidate = value
    total_appearances = 0
    for i in range(N):
        if A[i] == candidate:
            total_appearances += 1
	
	
    # Count the number of equi_leaders by determining whether candidate
    # is the dominant value in each splitting of the list
    appearances_lower = 0
    appearances_upper = total_appearances
    num_equi_leaders = 0
    for i in range(N):
        if appearances_lower > i/2 and appearances_upper > (N-i)/2:
            num_equi_leaders += 1
        if A[i] == candidate:
            appearances_lower += 1
            appearances_upper -= 1
	
    return num_equi_leaders


