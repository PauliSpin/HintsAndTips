x = [i for i in range(5)]
print(x)    # Creates the list [0, 1, 2, 3, 4]

x = [i for i in range(5) if i % 2 == 0]
print(x)    # Creates the list [[0, 2, 4]

# Nested lists
x = [[] for i in range(5)]
print(x)    # prints [[], [], [], [], []]

x = [[0, 1] for i in range(5)]
print(x)    # prints [[0, 1], [0, 1], [0, 1], [0, 1], [0, 1]]

x = [[j for j in range(i)] for i in range(5)]
print(x)    # prints [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]

x = [[x, y] for x, y in zip(range(5), range(5, 10))]
print(x)    # prints [0, 5], [1, 6], [2, 7], [3, 8], [4, 9]]

x = [x for x, y in zip(range(5), range(5, 10))]
print(x)    # prints [0, 1, 2, 3, 4]

x = [y for x, y in zip(range(5), range(5, 10))]
print(x)    # prints [5, 6, 7, 8, 9]

# Anonymous variable '_'
# In the above, the x is not being used so can substitute it for '_'
# Since '_' is just a place holder, it cannot be printed or used.
x = [y for _, y in zip(range(5), range(5, 10))]
print(x)    # prints [5, 6, 7, 8, 9]

for _ in range(5):
    print('Hello')
