import sys

x = 100
print(sys.getsizeof(x))  # prints 28 i.e. 100 requires 28 bytes in memory

x = 'hello'
print(sys.getsizeof(x))  # prints 54 i.e. 'hello' requires 54 bytes in memory

x = [1, 2, 3, 4]
print(sys.getsizeof(x))  # prints 88 i.e. 'hello' requires 88 bytes in memory
