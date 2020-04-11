'''

This text file can be used as a Python program,
script or module.

'''
import random

sayings = ('Hello', 'Hi', 'Hey', 'Aloha')


def greet():
    return random.choice(sayings)


def test_greet():
    # for loop in range(8): highlights the fact that loop is never used
    # so used '_' instead of 'loop'
    for _ in range(8):
        print(greet(), end=' ')
    print('\nGreetings Test Completed')


# If this module is run directly then the name will be __main__,
# however, if it is used as an imported module then it not print 'greet output'.
# So can use it inside modules for controlling printing etc.
if __name__ == '__main__':
    print(greet())
