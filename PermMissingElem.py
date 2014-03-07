# Solution to exercise PermMissingElem
# http://www.codility.com/train/

def solution(A):
    N = len(A)
    
    # The array with the missing entry added should sum to (N+2)(N+1)/2
    # so the missing entry can be determined by subtracting the sum of
    # the entries of A
    missing_element = (N+2)*(N+1)/2 - sum(A)
    
    return missing_element
