def solution(A, B):
    N = len(A)
    survivor_count = 0
    fish_downstream = []
    
    for i in range(N):
        if B[i] == 1:
            fish_downstream.append(A[i])
        if B[i] == 0:
            # if there are no fish left downstream then fish i survives
            if len(fish_downstream) == 0:
                survivor_count += 1
			
            # otherwise, it swims downstream eating the downstream fish until
            # it either gets eaten or reaches the end and survives
            else:
                while len(fish_downstream) > 0 and fish_downstream[-1] < A[i]:
                    fish_downstream.pop()
                if len(fish_downstream) == 0:
                    survivor_count += 1
	
    # all the fish in the fish_downstream list that have not
    # been eaten after all the fish swimming upstream pass also survive
    survivor_count = survivor_count + len(fish_downstream)
    
    return survivor_count