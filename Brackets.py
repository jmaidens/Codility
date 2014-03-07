# Solution to exercise Brackets
# http://www.codility.com/train/

def solution(S):
	
	# Create a stack to track what braces are open
    stack = []
    opposite_braces = {'(': ')',
		'{': '}',
		'[': ']'}
	
    for i in S:
		# Each time a brace is opened, add it to the stack
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
		# Each time a close brace appears, ensure that it corresponds to the correct opened brace
        else:
            if len(stack) == 0:
                return 0
            j = stack.pop()
            if not i == opposite_braces[j]:
                return 0
		
	# After the string has been traversed, the stack should be empty
    if len(stack) == 0:
        return 1
    else:
        return 0

