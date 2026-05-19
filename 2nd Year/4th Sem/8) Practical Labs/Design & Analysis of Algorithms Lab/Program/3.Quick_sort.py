print("Array is sorted using Quick Sort")
def quick_sort(arr): 
    if len(arr) <= 1: 
        return arr 
    pivot = arr[0] 
    left = [x for x in arr if x < pivot] 
    right = [x for x in arr if x > pivot] 
    middle = [x for x in arr if x == pivot] 
    return quick_sort(left) + middle + quick_sort(right)
# Example usage 
arr = [5,3,8,4,2] 
print("Unsorted array", arr) 
print("Sorted array:", quick_sort(arr))
