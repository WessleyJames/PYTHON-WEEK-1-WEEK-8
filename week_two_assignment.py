# file: week_two_assignment.py

# Step 1: Create an empty list
my_list = []

# Step 2: Append elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend with another list
my_list.extend([50, 60, 70])

# Step 5: Remove the last element
my_list.pop()

# Step 6: Sort list in ascending order
my_list.sort()

# Step 7: Find index of 30
index_of_30 = my_list.index(30)

# Output results
print("Final List:", my_list)
print("Index of 30:", index_of_30)
