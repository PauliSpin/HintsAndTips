my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9     Forward indeces
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1     Backward indeces

# List[start:end:step]

print(my_list[-1])   # Prints 9

print(my_list[-10])  # Prints 0

print(my_list[0:5])  # Prints [0, 1, 2, 3, 4] so 'end' index is non-inclusive

print(my_list[3:8])  # Prints [3, 4, 5, 6, 7]

print(my_list[-7:-2])  # Prints [3, 4, 5, 6, 7]

# Prints from index 1 to the end i.e. [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[1:])

print(my_list[2:-1])    # Prints [2, 3, 4, 5, 6, 7, 8]

print(my_list[2:-1:2])    # Prints [2, 4, 6, 8]

print(my_list[-1:2:-1])  # Prints [9, 8, 7, 6, 5, 4, 3]

# Prints [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] i.e. reverses the entire list
print(my_list[::-1])

sample_url = 'http://coreyms.com'
print(sample_url)

# Reverse the url
print(sample_url[::-1])  # Prints moc.smyeroc//:ptth

# Get the top level domain
print(sample_url[-4:])  # Prints .com

# Get the url without the http://
print(sample_url[7:])  # Prints coreyms.com
