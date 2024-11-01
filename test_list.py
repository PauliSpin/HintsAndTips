list_a = [1, 2, 3]
list_b = [4, 5, 6]

print(f"list_a = {list_a}")
print(f"list_b = {list_b}")
print(f"list_a + list_b = {list_a + list_b}")

def add_lists(list1, list2):
    # Check if both lists have the same number of elements
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same number of elements.")

    # Add corresponding elements of both lists
    result_list = [list1[i] + list2[i] for i in range(len(list1))]
    
    return result_list

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

result = add_lists(list1, list2)

print("\n")
print(f"list1         = {list1}")
print(f"list2         = {list2}")
print(f"list1 + list2 = {result}")
print("\n")
