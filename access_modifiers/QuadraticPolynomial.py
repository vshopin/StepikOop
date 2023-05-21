from math import sqrt


class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b - sqrt(self.b ** 2 - 4 * self.a * self.c)) / (2 * self.a)

    @property
    def x2(self):
        if self.b ** 2 - 4 * self.a * self.c < 0:
            return None
        else:
            return (-self.b + sqrt(self.b ** 2 - 4 * self.a * self.c)) / (2 * self.a)

    @property
    def view(self):
        b_str = f"{'+' if self.b >= 0 else '-'} {abs(self.b)}"
        c_str = f"{'+' if self.c >= 0 else '-'} {abs(self.c)}"
        return f"{self.a}x^2 {b_str}x {c_str}"

    @property
    def coefficients(self):
        return self.a, self.b, self.c

    @coefficients.setter
    def coefficients(self, arguments):
        self.a = arguments[0]
        self.b = arguments[1]
        self.c = arguments[2]


polynom = QuadraticPolynomial(1, 2, -3)

polynom.coefficients = (1, -5, 6)
print(polynom.x1)
print(polynom.x2)
print(polynom.view)
