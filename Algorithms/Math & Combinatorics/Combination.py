def CombinationIterative(elements: list, r: int) -> None:

    """Print all possible results of selecting r elements"""

    n = len(elements)

    if r > n or r < 1:
        return None
    
    indices = [num for num in range(r)] # The indices of elements that will be printed
    
    while True:
        current_combination = [] 
        
        for i in indices: # Add the elements that will be printed
            current_combination.append(elements[i])
        
        print(current_combination) # Print the combination

        
        #################### Preparing the indices
        i = r - 1 # l
        
        while i > -1 and indices[i] == n - r + i: # switch to the previous index if current index reach to its limit
            i = i - 1

        if i < 0: # End the process if the index switched to negative number
            break
        
        indices[i] = indices[i] + 1 # Increase the value of index after the switching
        
        for j in range(i + 1, r): # Rearrange the next indices after the Increasing to repeat the process 
            indices[j] = indices[j - 1] + 1
        ####################




elements = [1,2,3,4,5, 6]; r = 4
CombinationIterative(elements, r)