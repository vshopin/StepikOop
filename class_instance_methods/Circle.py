"""
Реализуйте класс Circle, описывающий круг. При создании экземпляра класс должен принимать один аргумент:
radius — радиус круга
Экземпляр класса Circle должен иметь три атрибута:
radius — радиус круга
diameter — диаметр круга
area — площадь круга
Примечание 1. Площадь круга вычисляется по формуле
pi * (r)2
"""


from math import pi, pow


class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
        self.area = pi * pow(radius, 2)


circle = Circle(5)

print(circle.radius)
print(circle.diameter)
print(circle.area)