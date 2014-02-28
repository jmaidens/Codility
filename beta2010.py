# Solution to exercise beta2010
# http://www.codility.com/train/

import bisect

def solution(A):
	# My solution uses the fact that, assuming the maximal endpoints A+ and B+ of circles A and B do not coincide, then A and B intersect if and only if A+ \in B xor B+ \in A. Therefore we can count the number of intersecting circles by iterating through circles and counting the number of maximal endpoints in each. This overcounts if some maximal endpoints coincide, so we must subtract a correction term, as explained below. 
    
    N = len(A)
	
	# construct a sorted array of the maximal endpoints of the circles
	# takes time O(N log N) and space O(N)
    upper_points = []
    for i in range(N):
        upper_points.append(i+A[i])
    upper_points.sort()
    
    # compute a correction due to repeated upper_points
    # if some integer k appears n times in upper_points, we overcount by n(n-1)/2
	# takes time O(N) and space O(1) 
    intersection_count = 0
    i = 0
    while(i < N):
        j = bisect.bisect_right(upper_points, upper_points[i])
        n = j - i
        intersection_count -= n*(n-1)/2
        i = j
    
	# loop through all circles and count the number of upper_points in each
	# at the end of loop, intersection_count is the number of intersections
	# bisection search can be performed in time O(log N) therefore loop takes times O(N log N) and space O(1) 
    for i in range(N):
        lower = i - A[i]
        upper = i + A[i]
        j = bisect.bisect_left(upper_points, lower)
        k = bisect.bisect_right(upper_points, upper)
        intersection_count += k - j - 1  ## check this
        print intersection_count
        if intersection_count > 10000000:
            return -1

    return intersection_count