# Solution to exercise PermCheck
# http://www.codility.com/train/

def solution(A):
    
    N = len(A)
    
    # Create an array of counts
    # B[i] counts the number of times i occurs in A
    
    B = [0 for _ in range(N+1)]
    
    # If A contains any entry outside the range 1 to N, or if any entry appears more than once, then A is not a permutation
    for a in A:
        if a < 1 or a > N or B[a] > 0:
            return 0
        else:
            B[a] = B[a] + 1

    return 1


