# https://www.youtube.com/watch?v=P0kfKqMHioQ

# Polymorphism allows us to replace if statements
# so that we do not have to keep checking the animal
# to see what it is in the speak() function to make it
# say either woof or meow.
# Adding a new type of animal means we can specifically
# tailor it to do what we want.


class Animal(object):
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Dog(Animal):
    def speak(self):
        return "Woof!"


canine = Cat("pussy")
feline = Dog("fido")

print(f'{canine.name} says {canine.speak()}')
print(f'{feline.name} says {feline.speak()}')

# the follwoing will not work because it each
# subclass will implement the speak method and not the parent
#   print(Animal("canine").speak()) returns:
#   NotImplementedError
