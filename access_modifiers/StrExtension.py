"""
Реализуйте класс StrExtension, описывающий набор функций для работы со строками. При создании экземпляра класс не должен принимать никаких аргументов.
Класс StrExtension должен иметь три статических метода:
remove_vowels() — метод, который принимает в качестве аргумента строку, удаляет из нее все гласные латинские буквы без учета регистра и возвращает полученный результат
leave_alpha() — метод, который принимает в качестве аргумента строку, удаляет из нее все символы, не являющиеся латинскими буквами, и возвращает полученный результат
replace_all() — метод, который принимает три строковых аргумента string, chars и char, заменяет в строке string все символы из chars на char с учетом регистра и возвращает полученный результат.
Примечание 1. Гарантируется, что все буквенные символы относятся к латинскому алфавиту.
Примечание 2. Латинские гласные буквы: a, e, i, o, u, y.
Примечание 3. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""
import string

class StrExtension:
    def __init__(self):
        pass

    @staticmethod
    def remove_vowels(input_str):
        list_for_check = [char for char in list(input_str) if char.lower() not in "aeiouy"]
        return "".join(list_for_check)

    @staticmethod
    def leave_alpha(input_str):
        list_for_check = [char for char in list(input_str) if char.lower() in string.ascii_lowercase]
        return "".join(list_for_check)

    @staticmethod
    def replace_all(string, chars, char):
        return ''.join(map(lambda i: char if i in chars else i, string))


print(StrExtension.leave_alpha('Python111'))
print(StrExtension.leave_alpha('__Stepik__()'))
