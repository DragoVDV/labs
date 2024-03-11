def find_unsorted_subarray(arr):
    n = len(arr)
    if n <= 1:
        return (-1, -1)
    
    start = 0
    while start < n - 1 and arr[start] <= arr[start + 1]:
        start += 1
    if start == n - 1: 
        return (-1, -1)   
    
    end = n - 1
    while end > 0 and arr[end] >= arr[end - 1]:
        end -= 1

    min_val = min(arr[start:end + 1])
    max_val = max(arr[start:end + 1])
        
    while start > 0 and arr[start - 1] > min_val:
        start -= 1
    while end < n - 1 and arr[end + 1] < max_val:
        end += 1
    
    return (start,end)


nums = [1,2,4,3,5]
result = find_unsorted_subarray(nums)
print(result)  
