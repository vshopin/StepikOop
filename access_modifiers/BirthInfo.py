"""
Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один аргумент:
birth_date — дата рождения, представленная в одном из следующих вариантов:
экземпляр класса date
строка с датой в ISO формате
список или кортеж из трех целых чисел: года, месяца и дня
Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение TypeError с текстом:
Аргумент переданного типа не поддерживается
Экземпляр класса BirthInfo должен иметь один атрибут:
birth_date — дата рождения в виде экземпляра класса date
Класс BirthInfo должен иметь одно свойство:
age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет, прошедших с даты рождения на сегодняшний день
Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его возраст увеличивается на один год.
"""
from datetime import date


class BirthInfo:
    def __init__(self, birth_date):
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            try:
                self.birth_date = date.fromisoformat(birth_date)
            except ValueError:
                raise TypeError('Аргумент переданного типа не поддерживается')
        elif isinstance(birth_date, (list, tuple)):
            if len(birth_date) == 3:
                self.birth_date = date(birth_date[0], birth_date[1], birth_date[2])
        else:
            raise TypeError('Аргумент переданного типа не поддерживается')

    @property
    def age(self):
        today = date.today()
        return today.year - self.birth_date.year


def current_age(birthday, today):
    if isinstance(birthday, date) and isinstance(today, date):
        return today.year - birthday.year
    else:
        raise TypeError


birth_dates = ['20200918', '2020-0918', '202009-18', ' 2020-09-18 ', '2020-9-18']

for birth_date in birth_dates:
    try:
        birthinfo1 = BirthInfo(birth_date)
    except TypeError as e:
        print(e)