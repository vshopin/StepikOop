"""
Реализуйте класс Person, описывающий человека. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
name — имя человека
surname — фамилия человека
Экземпляр класса Person должен иметь два атрибута:
name — имя человека
surname — фамилия человека
Класс Person должен иметь одно свойство:
fullname — свойство, доступное для чтения и записи, возвращающее полное имя человека в виде строки:
<имя> <фамилия>
Примечание 1. При изменении имени и/или фамилии человека должно изменяться и его полное имя. Аналогично при изменении полного имени должны изменяться имя и фамилия.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Person:
    def __init__(self, person_name, person_surname):
        self.name = person_name
        self.surname = person_surname

    def get_name(self):
        return self._name

    def get_surname(self):
        return self._surname

    def set_name(self, new_name):
        self._name = new_name

    def set_surname(self, new_surname):
        self._surname = new_surname

    def get_fullname(self):
        return self._name + " " + self._surname

    def set_fullname(self, fullname):
        self._fullname = " ".join(fullname.split())
        self._name = fullname.split()[0]
        self._surname = fullname.split()[1]

    name = property(get_name, set_name)
    surname = property(get_surname, set_surname)
    fullname = property(get_fullname, set_fullname)


person = Person('Меган', 'Фокс')

person.name = 'Стефани'
print(person.fullname)
