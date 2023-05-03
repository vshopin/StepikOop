"""
Реализуйте класс Bee, описывающий пчелку, которая перемещается по координатной плоскости в четырех направлениях: вверх,
вниз, влево и вправо. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
x — координата пчелки по оси x
x, по умолчанию имеет значение 0
y — координата пчелки по оси y
y, по умолчанию имеет значение 0
Экземпляр класса Bee должен иметь два атрибута:
x — координата пчелки по оси x
y — координата пчелки по оси y
Класс Bee должен иметь четыре метода экземпляра:
move_up() — метод, принимающий в качестве аргумента целое число n и увеличивающий координату пчелки по оси y на n
move_down() — метод, принимающий в качестве аргумента целое число n и уменьшающий координату пчелки по оси y на n
move_right() — метод, принимающий в качестве аргумента целое число n и увеличивающий координату пчелки по оси x на n
move_left() — метод, принимающий в качестве аргумента целое число n и уменьшающий координату пчелки по оси x на n
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Bee:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_up(self, n: int):
        self.y += n

    def move_down(self, n: int):
        self.y -= n

    def move_right(self, n: int):
        self.x += n

    def move_left(self, n: int):
        self.x -= n


bee = Bee()

bee.move_right(2)
bee.move_right(2)
bee.move_up(3)
bee.move_left(1)
bee.move_down(1)

print(bee.x, bee.y)
