"""
Реализуйте класс Knight, описывающий шахматного коня. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
horizontal — координата коня по горизонтали, представленная латинской буквой от a до h
vertical — координата коня по вертикали, представленная целым числом от 1 до 8 включительно
color — цвет коня (black или white)
Экземпляр класса Knight должен иметь три атрибута:
horizontal — координата коня на шахматной доске по горизонтали
vertical — координата коня на шахматной доске по вертикали
color — цвет коня
Класс Knight должен иметь четыре метода экземпляра:
get_char() — метод, возвращающий символ N
can_move() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали, и возвращающий True, если конь может переместиться на клетку с данными координатами, или False в противном случае
move_to() — метод, принимающий в качестве аргументов координаты клетки по горизонтали и по вертикали и заменяющий текущие координаты коня на переданные. Если конь из текущей клетки не может переместиться на клетку с указанными координатами, его координаты должны остаться неизменными
draw_board() — метод, печатающий шахматное поле, отмечающий на этом поле коня и клетки, на которые может переместиться конь. Пустые клетки должны быть отображены символом ., конь — символом N, клетки, на которые может переместиться конь, — символом *
"""


class Knight:
    def __init__(self, horizontal, vertical, color):
        self.horizontal = horizontal
        self.vertical = vertical
        self.color = color
        self.check_dict = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }

    def __check_move(self, test_char):
        for char in self.check_dict:
            if char == test_char:
                return self.check_dict[test_char]

    def get_char(self) -> str:
        return "N"

    def can_move(self, input_horizontal: str, input_vertical: int) -> bool:
        if ((abs(self.__check_move(self.horizontal) - self.__check_move(input_horizontal)) == 1) and (
                abs(self.vertical - input_vertical) == 2)) or (
                abs(self.__check_move(self.horizontal) - self.__check_move(input_horizontal)) == 2) and (
                abs(self.vertical - input_vertical) == 1):
            return True
        else:
            return False

    def move_to(self, input_horizontal: str, input_vertical: int):
        if self.can_move(input_horizontal, input_vertical):
            self.horizontal = input_horizontal
            self.vertical = input_vertical

    def draw_board(self):
        col, row = self.horizontal, str(self.vertical)
        coor_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
        coor_row = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
        arr = [["N" if [i, j] == [coor_row[row], coor_col[col]] else '.' for j in range(8)] for i in range(8)]
        for i in range(8):
            for j in range(8):
                if (coor_row[row] - i) * (coor_col[col] - j) in [-2, 2]:
                    arr[i][j] = "*"
        for line in arr:
            print(*line, sep='')


knight = Knight('c', 3, 'white')

knight.draw_board()


