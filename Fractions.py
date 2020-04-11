class fraction(object):
    """
    A number represented as a fraction
    """

    def __init__(self, num, den):
        """ num and den are integers """
        assert type(num) == int and type(den) == int, "Must be integers"
        self.num = num
        self.den = den

    def __str__(self):
        """ Returns a string representation of the fraction """
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        """ Returns a new fraction representing the sum """
        top = self.num * other.den + self.den * other.num
        bot = self.den * other.den
        return fraction(top, bot)

    def __sub__(self, other):
        """ Returns a new fraction representing the sum """
        top = self.num * other.den - self.den * other.num
        bot = self.den * other.den
        return fraction(top, bot)

    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num / self.den

    def inverse(self):
        """ Returns a new fraction representing the inverse """
        return fraction(self.den, self.num)


f1 = fraction(1, 4)
f2 = fraction(3, 4)
print(f1)
print(f2)

f3 = f1 + f2
print(f3)
print(fraction.__float__(f3))
print(f2.inverse())
print(float(f2.inverse()))
