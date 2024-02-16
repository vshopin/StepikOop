"""
Реализуйте класс Formatter. При создании экземпляра класс не должен принимать никаких аргументов.
Класс Formatter должен иметь один статический метод:
format() — метод, принимающий в качестве аргумента объект типа int, float, tuple, list или dict и
выводящий информацию о переданном объекте в формате, зависящем от его типа.
Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение
TypeError с текстом: Аргумент переданного типа не поддерживается

Примечание 1. Примеры форматирования объектов всех типов показаны в тестовых данных.
Примечание 2. Обратите внимание, что метод format() должен обрамлять апострофами строковые
элементы коллекций.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что
реализованный класс используется только с корректными данными.
Примечание 4. Никаких ограничений касательно реализации класса Formatter нет, она может быть
произвольной.
"""

from functools import singledispatchmethod
from typing import Any


class Formatter:
    @singledispatchmethod
    @staticmethod
    def format(obj: Any):
        raise TypeError("Аргумент переданного типа не поддерживается")

    @format.register(int)
    @staticmethod
    def _(obj: Any):
        print(f"Целое число: {obj}")

    @format.register(float)
    @staticmethod
    def _(obj: Any):
        print(f"Вещественное число: {obj}")

    @format.register(tuple)
    @staticmethod
    def _(obj: Any):
        print(f"Элементы кортежа: {', '.join(map(str, obj))}")

    @format.register(list)
    @staticmethod
    def _(obj: Any):
        print(f"Элементы списка: {', '.join(map(str, obj))}")

    @format.register(dict)
    @staticmethod
    def _(obj: Any):
        print(f"Пары словаря: {', '.join(map(str, zip(obj.keys(), obj.values())))}")


Formatter.format({1: 'one', 2: 'two'})

