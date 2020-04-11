names = ['Tim', 'Bill', "Joe"]
ages = [19, 64, 34, 76]  # sic.
fav_colour = ['blue', 'red', 'green']

for i in range(len(names)):
    print(names[i], ages[i], fav_colour[i])
# Prints the following, where the fourth element in ages is not used
# because the len(names) = 3
# Tim 19 blue
# Bill 64 red
# Joe 34 green

#
# zip creates tuples of pairs using the minimum len of the lists passed in
print(list(zip(names, ages, fav_colour)))
# prints
# [('Tim', 19, 'blue'), ('Bill', 64, 'red'), ('Joe', 34, 'green')]

# can loop through these:
for name, age, colour in zip(names, ages, fav_colour):
    print(name, age, colour)

# which prints:
# Tim 19 blue
# Bill 64 red
# Joe 34 green
