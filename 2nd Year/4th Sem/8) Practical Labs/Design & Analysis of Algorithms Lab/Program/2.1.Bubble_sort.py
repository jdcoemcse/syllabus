list1 = [9, 16, 6, 26, 0] 
print("Unsorted list1 is", list1) 
# Bubble sort 
for j in range(len(list1) - 1):  # Outer loop 
    for i in range(len(list1) - 1):  # Inner loop 
        if list1[i] > list1[i + 1]:  # Compare adjacent elements 
            list1[i], list1[i + 1] = list1[i + 1], list1[i] 
    print("List after iteration", j + 1, "is", list1)  # Print list after each outer loop iteration 
 
print("\nSorted list is", list1) 