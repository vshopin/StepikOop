"""
Реализуйте класс Todo, описывающий список дел. При создании экземпляра класс не должен принимать никаких аргументов.
Экземпляр класса Todo должен иметь один атрибут:
things — изначально пустой список дел, которые нужно выполнить
Класс Todo должен иметь четыре метода экземпляра:
add() — метод, принимающий название дела и его приоритет (целое число) и добавляющий данное дело в список дел в виде кортежа:
(<название дела>, <приоритет>)
get_by_priority() — метод, принимающий в качестве аргумента целое число n и возвращающий список названий дел, имеющих приоритет n
get_low_priority() — метод, возвращающий список названий дел, имеющих самый низкий приоритет
get_high_priority() — метод, возвращающий список названий дел, имеющих самый высокий приоритет
Примечание 1. Названия дел в списках, возвращаемых методами get_by_priority(), get_low_priority() и get_high_priority(), должны располагаться в том порядке, в котором они были добавлены в список.
Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
"""


class Todo:
    def __init__(self):
        self.things = []
        self.low = 0
        self.high = 0

    def __get_list_of_priority(self, list_of_priority: list) -> list:
        return [i[1] for i in list_of_priority]

    def add(self, todo_name: str, priority: int) -> None:
        self.things.append((todo_name, priority))

    def get_by_priority(self, n: int) -> list:
        return [todo_name[0] for todo_name in self.things if todo_name[1] == n]

    def get_low_priority(self) -> list:
        return [todo_name[0] for todo_name in self.things if
                todo_name[1] == min(self.__get_list_of_priority(self.things))]

    def get_high_priority(self) -> list:
        return [todo_name[0] for todo_name in self.things if
                todo_name[1] == max(self.__get_list_of_priority(self.things))]


todo = Todo()

todo.add('Ответить на вопросы', 5)
todo.add('Сделать картинки', 1)
todo.add('Доделать задачи', 4)
todo.add('Дописать конспект', 5)

print(todo.get_low_priority())
print(todo.get_high_priority())
print(todo.get_by_priority(3))
