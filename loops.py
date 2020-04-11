x = [2, 3, 4, 5]

# Want to print theindex and the value in x at that index
for i in range(len(x)):
    print(i, x[i])

print()

# Can use the enumerate function to write out the index and the value at the same time

for i, element in enumerate(x):
    # This avoids having to reference x[i] which is a bit ugly
    print(i, element)
