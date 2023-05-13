"""
Реализуйте класс TextHandler, описывающий изначально пустой расширяемый набор слов. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса TextHandler должен иметь три метода:
add_words() — метод, принимающий в качестве аргумента текст и добавляющий слова из данного текста в набор
get_shortest_words() — метод, возвращающий актуальный список самых коротких слов в наборе
get_longest_words() — метод, возвращающий актуальный список самых длинных слов в наборе
Примечание 1. Слова в списках, возвращаемых методами get_shortest_words() и get_longest_words(), должны располагаться в том порядке, в котором они были добавлены в набор.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""


class TextHandler:
    def __init__(self):
        self.words = []
        self.shortest = 0
        self.longest = 0

    def add_words(self, words):
        words = words.split()
        self.words.extend(words)

    def get_shortest_words(self):
        try:
            self.shortest = min(map(len, self.words))
        except ValueError:
            pass
        return [word for word in self.words if len(word) == self.shortest]

    def get_longest_words(self):
        try:
            self.longest = max(map(len, self.words))
        except ValueError:
            pass
        return [word for word in self.words if len(word) == self.longest]


texthandler = TextHandler()

print(texthandler.get_shortest_words())
print(texthandler.get_longest_words())
