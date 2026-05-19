class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Compute value-to-weight ratio

def knapsack_greedy(items, capacity):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0  
    for item in items:
        if capacity >= item.weight:  # If the item can be fully included
            total_value += item.value
            capacity -= item.weight
        else:  # If only a fraction of the item can be included
            total_value += item.ratio * capacity
            break  # Knapsack is full

    return total_value

# Taking user input
n = int(input("Enter number of items: "))
items = []

for i in range(n):
    value, weight = map(int, input(f"Enter value and weight of item {i+1}: ").split())
    items.append(Item(value, weight))

capacity = int(input("Enter knapsack capacity: "))

# Compute the maximum value that can be obtained
max_value = knapsack_greedy(items, capacity)
print("Maximum value in Knapsack:", max_value)
