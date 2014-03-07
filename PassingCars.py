# Solution to exercise PassingCars
# http://www.codility.com/train/

def solution(A):
	
	# Create a list of cars remaining to be passed by a car moving west in i-th position 
	cars_remaining_to_west = [0]
	for i in range(1,len(A)):
		if A[i-1] == 0:
			cars_remaining_to_west.append(1 + cars_remaining_to_west[-1])
		else:
			cars_remaining_to_west.append(cars_remaining_to_west[-1])

	# Loop through cars going west and count the number of passes they make
	num_passes = 0
	for i in range(len(A)):
		if A[i] == 1:
			num_passes += cars_remaining_to_west[i]
			if num_passes > 1000000000:
				return -1

	return num_passes
