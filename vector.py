
class Vector(object):
    ''' A class for 2D vectors which implements vector addition '''

    def __init__(self, x, y):
        ''' Inialise the vector object '''
        self.x = x
        self.y = y

    def __add__(self, other):
        ''' Implement the method for the "+" operator '''
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        ''' Implement the method for the "+" operator '''
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __repr__(self):
        ''' Provide an informative representation of the vector object '''
        return 'Vector(' + str(self.x) + ', ' + str(self.y) + ')'


u = Vector(3, 4)
v = Vector(5, 6)
a = u + v
s = u - v

print(u)
print(v)
print(a)
print(s)
