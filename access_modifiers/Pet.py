"""
Реализуйте класс Pet, описывающий домашнее животное. При создании экземпляра класс должен принимать один аргумент:
name — имя домашнего животного
Экземпляр класса Pet должен иметь один атрибут:
name — имя домашнего животного
Класс Pet должен иметь три метода класса:
first_pet() — метод, возвращающий самый первый созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
last_pet() — метод, возвращающий самый последний созданный экземпляр класса Pet. Если ни одного экземпляра еще не было создано, метод должен вернуть значение None
num_of_pets() — метод, возвращающий количество созданных экземпляров класса Pet
Примечание 1. Никаких ограничений касательно реализации класса Pet нет, она может быть произвольной.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Pet:
    first_pet_instance = None
    last_pet_instance = None
    num_of_pets_created = 0

    def __init__(self, name):
        self.name = name
        if Pet.first_pet_instance is None:
            Pet.first_pet_instance = self
        Pet.last_pet_instance = self
        Pet.num_of_pets_created += 1

    @classmethod
    def first_pet(cls):
        return cls.first_pet_instance

    @classmethod
    def last_pet(cls):
        return cls.last_pet_instance

    @classmethod
    def num_of_pets(cls):
        return cls.num_of_pets_created


print(Pet.first_pet())
print(Pet.last_pet())
print(Pet.num_of_pets())