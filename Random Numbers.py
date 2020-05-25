import random
""" Perfect for random numbers and data - NOT for Security """

value = random.random()

# prints a random number between 0 and <1 i.e. not including 1. e.g. 0.4463492298050328
print(value)

value = random.uniform(1, 10)  # Prints 6.697678836077431 i.e. not integers

print(value)

# Simulate a 6-sided die
# Prints a random integer between 1 and 6 inclusive
value = random.randint(1, 6)
print(value)

# Random value picked from a list of values using the Choice method

greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']

value = random.choice(greetings)
print(value)

# Multiple choices also

colors = ['Red', 'Black', 'Green']

# Even weighting on 10 choices that are made
results = random.choices(colors, k=10)

print(results)
# ['Green', 'Black', 'Red', 'Red', 'Red', 'Red', 'Red', 'Black', 'Black', 'Red']

# Can set the weighting on the colors
# 18+18+2=38, so Red has a 18/38 chance of being picked, Black 18/38 and Green 2/38
results = random.choices(colors, k=10, weights=[18, 18, 2])
# So Green is least likely to be picked.
# ['Black', 'Red', 'Black', 'Red', 'Red', 'Red', 'Black', 'Black', 'Black', 'Red']
print(results)

# Randomly shuffle a list of values (say 52 Cards)

deck = list(range(1, 53))
# Creates:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
# 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
# 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
# 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46,
# 47, 48, 49, 50, 51, 52]
print(deck)

# Shuffles the list in place
random.shuffle(deck)

# [28, 26, 11, 32, 6, 31, 7, 37, 12, 49, 34,
# 18, 4, 52, 25, 20, 19, 41, 44, 30, 9, 45,
# 3, 42, 35, 36, 48, 5, 14, 24, 29, 43, 1, 47,
# 23, 38, 27, 51, 10, 2, 33, 22, 39, 17, 15,
# 50, 8, 46, 13, 21, 16, 40]

print(deck)

# Want to get 5 random cards from this deck - can't use Choices method as
# it may pick the same card multiple times. Better to use sample method

hand = random.sample(deck, k=5)  # Random Sample of 5 cards from the deck
print(hand)  # Prints [17, 7, 49, 30, 52]


# Generating Random Data - Other websites are available though
