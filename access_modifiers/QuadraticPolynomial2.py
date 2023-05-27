class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_iterable(cls, obj):
        return cls(obj[0], obj[1], obj[2])

    @classmethod
    def from_str(cls, input_str):
        list_args_for_obj = [float(arg) for arg in input_str.split(" ")]
        return cls(list_args_for_obj[0], list_args_for_obj[1], list_args_for_obj[2])


polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')

print(polynom.a)
print(polynom.b)
print(polynom.c)
print(polynom.a + polynom.b + polynom.c)
