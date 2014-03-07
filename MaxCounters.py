# Solution to exercise MaxCounters
# http://www.codility.com/train/

def solution(N, A):
    
    counters = [0 for _ in range(N)]
    last_max_counter = 0
    current_max_counter = 0
    
    # Iterate through A. At each step, the value of counter i is
    # last_max_counter or counters[i], whichever is greater
    
    for a in A:
        if a == N+1:
            last_max_counter = current_max_counter
        elif counters[a-1] < last_max_counter:
            counters[a-1] = last_max_counter + 1
            current_max_counter = max(current_max_counter, counters[a-1])
        else:
            counters[a-1] += 1
            current_max_counter = max(current_max_counter, counters[a-1])

    # Make a pass through counters to update the ones that
    # have not changed since the last max_counter opperation
    
    for i in range(N):
        if counters[i] < last_max_counter:
            counters[i] = last_max_counter

    return counters