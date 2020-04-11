class Enum1:
    alpha, beta, gamma = range(3)   # range is 0 1 2


class Enum2:
    Tom, Dick, Harry = range(1, 4)  # range is 1 2 3


print(f'alpha = {Enum1.alpha}')
print(f'beta  = {Enum1.beta}')
print(f'gamma = {Enum1.gamma}')

print()
print(f'Tom   = {Enum2.Tom}')
print(f'Dick  = {Enum2.Dick}')
print(f'Harry = {Enum2.Harry}')
