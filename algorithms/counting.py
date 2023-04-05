def counting(lst, draw_list, GREEN, RED):
    # Determine the range of values in the list
    min_val = min(lst)
    max_val = max(lst)
    
    # Initialize the count array
    count = [0] * (max_val - min_val + 1)
    
    # Count the occurrences of each value in the list
    for val in lst:
        count[val - min_val] += 1
        
    # Reconstruct the sorted list using the count array
    i = 0
    for val in range(min_val, max_val + 1):
        for j in range(count[val - min_val]):
            lst[i] = val
            i += 1
            draw_list(lst, {i - 1: GREEN}, True)
            yield True
    
    return lst
