"""
Вам доступен класс Person, описывающий человека. При создании экземпляра класс принимает два аргумента в следующем порядке:
name — имя человека
surname — фамилия человека
Экземпляр класса Person имеет два атрибута:
name — имя человека
surname — фамилия человека
Класс Person имеет одно свойство:
fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
<имя> <фамилия>
Реализуйте свойство fullname класса Person с помощью декоратора @property.
Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя. Аналогично при изменении полного имени должны изменяться имя и фамилия.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Person:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, surname):
        self._surname = surname

    @property
    def fullname(self):
        return self._name + " " + self._surname

    @fullname.setter
    def fullname(self, fullname):
        self._fullname = " ".join(fullname.split())
        self._name = fullname.split()[0]
        self._surname = fullname.split()[1]


person = Person('Mike', 'Pondsmith')

person.fullname = 'Troy Baker'
print(person.name)
print(person.surname)
