x = [1, 2, 3, 4, 5]

print(*x)   # prints 1 2 3 4 5
# * is theunpack operator and print(*x) prints unpack and prints out the elements of the list

# This is used in arguments to functions and can be used
# to pass an unlimited number of arguments


def func(*args):
    print(args)


func(2, 3)          # prints the tuple (2, 3)
func(8, 7, 6, 5, 3)  # prints the tuple (8, 7, 6, 5, 3)

# This operator work ondictionaries as well:


def func2(*args, **kwargs):
    # this has taken a dictionary and uses the key as the name and the value as the value of the argument
    print(args, kwargs)
    print(type(args), type(kwargs))


func2(2, 3, k=0, x=8, hey=10)
# prints
#   (2, 3) {'k': 0, 'x': 8, 'hey': 10}
#   <class 'tuple'> <class 'dict'>
