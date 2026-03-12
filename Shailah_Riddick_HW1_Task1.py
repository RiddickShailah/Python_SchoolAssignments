#Shailah_Riddick_HW1_Task1
def next_greater_element(arr):
    stack = []
    result = [-1] * len(arr)
    
    # Traverse from right to left
    for i in range(len(arr) - 1, -1, -1):
        
        # Remove elements smaller than or equal to current
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        
        # If stack is not empty, top is next greater
        if stack:
            result[i] = stack[-1]
        
        # Push current element
        stack.append(arr[i])
    
    return result


#Driver Code
arr = [2, 1, 4, 3]
print(next_greater_element(arr))