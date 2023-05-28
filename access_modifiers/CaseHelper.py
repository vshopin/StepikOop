"""
Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.
Upper Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.
Реализуйте класс CaseHelper, описывающий набор функций для работы со строками в стилях Snake Case и Upper Camel Case. При создании экземпляра класс не должен принимать никаких аргументов.
Класс CaseHelper должен иметь четыре статических метода:
is_snake() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Snake Case, или False в противном случае
is_upper_camel() — метод, принимающий в качестве аргумента строку и возвращающий True, если переданная строка записана в стиле Upper Camel Case, или False в противном случае
to_snake() — метод, который принимает в качестве аргумента строку в стиле Upper Camel Case, записывает ее в стиле Snake Case и возвращает полученный результат
to_upper_camel() — метод, который принимает в качестве аргумента строку в стиле Snake Case, записывает ее в стиле Upper Camel Case и возвращает полученный результат
Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""


class CaseHelper:
    def __init__(self):
        pass

    @staticmethod
    def is_snake(input_string):
        if not input_string.islower():
            return False
        if input_string[0] == "_" or input_string[len(input_string)-1] == "_":
            return False
        try:
            input_string.split("_")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_upper_camel(input_string):
        if not input_string[0].isupper():
            return False
        try:
            test = input_string.split(" ")
            for i in test:
                if not i.isalpha() or i.islower():
                    return False
            return True
        except ValueError:
            return False

    @staticmethod
    def to_snake(input_string):
        snake_list = list(input_string)
        snake_list[0] = snake_list[0].lower()
        for i in range(1, len(snake_list) - 1):
            if snake_list[i].isupper():
                snake_list[i] = snake_list[i].lower()
                snake_list[i-1] = snake_list[i-1] + "_"
        return "".join(snake_list)

    @staticmethod
    def to_upper_camel(input_string):
        camel_list = input_string.split("_")
        for i in range(len(camel_list)):
            camel_list[i] = camel_list[i].capitalize()
        return "".join(camel_list)


cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp']

for case in cases:
    print(CaseHelper.is_upper_camel(case))

