def find_max_min(numbers):
    max_value = min_value = numbers[0]  # Initialize with the first element

    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

# Taking user input
numbers = list(map(int, input("Enter integers separated by spaces: ").split()))

# Finding max and min
maximum, minimum = find_max_min(numbers)

# Displaying results
print("Maximum value:", maximum)
print("Minimum value:", minimum)
