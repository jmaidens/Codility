def solution(H):
    stack_of_heights = [0]
    blocks_needed = 0
    for h in H:
        # if the wall is too tall to the left of current section, 
        # we must end all previous blocks that are too tall
        if h < stack_of_heights[-1]:
            while stack_of_heights[-1] > h:
                stack_of_heights.pop()
        # if the wall is not tall enough, you will need a new block 
        if h > stack_of_heights[-1]:
            blocks_needed += 1
            stack_of_heights.append(h)
        
    return blocks_needed