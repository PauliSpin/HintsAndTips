
# returns 99 as it is the largest of the elements in the list
print(max(1, 2, 99, 3, 4, 5))

x = [1, 2, 3, 4, 4, 5, 5, 6, 6, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 5]
print(set(x))   # prints {1, 2, 3, 4, 5, 6}

# max(set(x), key=x.count) for each element of the set(x), counts how many there are

print(max(set(x), key=x.count))
# x.count is usually written with brackes as x.count(),
# but here it is a function being passed using key=
# Pick the max from the set 'x' and count
# This returns 1 as it is the most frequent element in the list

x = [1, 2, 3, 4, 4, 5, 5, 6, 6, 2, 2, 2, 3, 4, 5]
# prints 2 as it is now the most frequent element in the list
print(max(set(x), key=x.count))

# Using lambda function
x = [(1, 2), (3, 4), (1, 9)]
# Want to pick the largest element in the list based on the second value
# prints (1, 9) since the 1th element that is the largest is in (1, 9)
print(max(x, key=lambda y: y[1]))
# the lambda functiontakes one argument y and then returns its 1th element
