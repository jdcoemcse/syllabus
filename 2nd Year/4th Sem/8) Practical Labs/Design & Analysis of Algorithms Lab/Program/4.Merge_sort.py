def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the elements into 2 halves
        right_half = arr[mid:]
        
        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half
        
        i = j = k = 0
        
        # Copy data to temp arrays left_half and right_half
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def merge_and_sort_lists(list1, list2):
    merged_list = list1 + list2  # Merging two lists
    merge_sort(merged_list)  # Sorting using merge sort
    return merged_list

# Taking user input for two lists
list1 = list(map(int, input("Enter elements of first list separated by spaces: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by spaces: ").split()))

sorted_list = merge_and_sort_lists(list1, list2)
print("List 1 is:", list1)
print("List 2 is:", list2)
print("Sorted Merged List:", sorted_list)
