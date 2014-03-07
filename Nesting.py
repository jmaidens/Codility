# Solution to exercise Brackets
# http://www.codility.com/train/

def solution(S):
	# Track the number of open nestings.
	# A properly nested string will never have a negative number of open nestings,
	# and all nestings will be closed by the end of the string.
    number_open = 0
    for s in S:
        if s == '(':
            number_open += 1
        if s == ')':
            number_open -= 1
            if number_open < 0:
                return 0
    
    if number_open == 0:
        return 1
	
    return 0
