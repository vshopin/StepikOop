"""
Реализуйте класс Config, который соответствует шаблону синглтон и описывает конфигурационный объект с фиксированными параметрами. При создании экземпляра класс не должен принимать никаких аргументов.
При первом вызове класса Config должен создаваться и возвращаться экземпляр этого класса, а при последующих вызовах должен возвращаться экземпляр, созданный при первом вызове.
Экземпляр класса Config должен иметь четыре атрибута:
program_name — атрибут со строковым значением GenerationPy
environment — атрибут со строковым значением release
loglevel — атрибут со строковым значением verbose
version — атрибут со строковым значением 1.0.0
Примечание 1. Подробнее почитать про шаблон проектирования синглтон можно по ссылке.
Примечание 2. Никаких ограничений касательно реализации класса Config нет, она может быть произвольной.
"""


class Config:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, program_name='GenerationPy', environment='release', loglevel='verbose',
                 version='1.0.0'):
        self.program_name = program_name
        self.environment = environment
        self.loglevel = loglevel
        self.version = version


config = Config()

print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)
