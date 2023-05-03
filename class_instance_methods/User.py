"""
Вам доступен класс User, описывающий интернет-пользователя. При создании экземпляра класс принимает один аргумент:
name — имя пользователя
Экземпляр класса User имеет два атрибута:
name — имя пользователя
friends — количество друзей пользователя, начальным значением является 0
Класс User имеет один метод экземпляра:
add_friends() — метод, принимающий в качестве аргумента целое число n и увеличивающий количество друзей пользователя на n
Найдите и исправьте ошибки, допущенные при реализации метода add_friends().

class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(n):
        friends += n
"""


class User:
    def __init__(self, name):
        self.name = name
        self.friends = 0

    def add_friends(self, n):
        self.friends += n


user = User('Arthur')
print(user.friends)
