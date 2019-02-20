def gcd(m, n):
    while m % n != 0:
        oldm = m
        m = n
        n = oldm % n
    return n


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        common = gcd(new_num, new_den)
        return Fraction(new_num // common, new_den // common)

    def __eq__(self, other):
        return self.num * other.den == self.den * other.num


if __name__ == '__main__':
    a = Fraction(3, 5)
    b = Fraction(1, 5)
    print(a + b)
