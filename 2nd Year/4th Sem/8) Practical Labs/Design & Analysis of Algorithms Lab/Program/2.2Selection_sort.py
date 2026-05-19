def selection_sort(arr): 
    # Traverse through all array elements 
    for i in range(len(arr)): 
        min_index = i  # Assume the current index as the minimum 
        # Find the minimum element in the remaining unsorted array 
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr[min_index]: 
                min_index = j  # Update the minimum index if a smaller element is found 
        # Swap the found minimum element with the first element of the unsorted part 
        arr[i], arr[min_index] = arr[min_index], arr[i] 
 
# Example usage 
arr = [64, 25, 12, 22, 11] 
print("Original array:", arr) 
selection_sort(arr) 
print("Sorted array:", arr)