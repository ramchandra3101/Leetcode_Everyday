def max_consistent_subarray_length(userEvent):
    n = len(userEvent)
    
    # Step 1: Calculate the minimum frequency in the whole array
    frequency = {}
    for user in userEvent:
        if user in frequency:
            frequency[user] += 1
        else:
            frequency[user] = 1
    min_frequency = min(frequency.values())
    print(frequency)
    
    # Step 2: Find the longest consistent subarray
    max_length = 0
    start = 0
    window_frequency = {}
    
    for end in range(n):
        if userEvent[end] in window_frequency:
            window_frequency[userEvent[end]] += 1
        else:
            window_frequency[userEvent[end]] = 1
      
        
        # Check if the current window is consistent
        while max(window_frequency.values(), default=0) > min_frequency:
            window_frequency[userEvent[start]] -= 1
            if window_frequency[userEvent[start]] == 0:
                del window_frequency[userEvent[start]]
            start += 1
        
        # Update the maximum length of the consistent subarray
        if max(window_frequency.values(), default=0) == min_frequency:
            max_length = max(max_length, end - start + 1)
    
    return max_length

# Example usage
n = 10
userEvent = [1, 2, 1, 3, 4, 2, 4, 3, 3, 4]
print(max_consistent_subarray_length(userEvent))  # Output: 8
