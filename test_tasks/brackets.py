"""
Назовем скобочной последовательностью строку, состоящую из символов ( и ). Будем считать скобочную последовательность
правильной, если:
для каждой открывающей скобки есть закрывающая скобка
скобки закрываются в правильном порядке, то есть в каждой паре из открывающей и закрывающей скобок открывающая находится левее
Напишите программу, которая определяет, является ли скобочная последовательность правильной.

Формат входных данных
На вход программе подается строка, представляющая собой скобочную последовательность.

Формат выходных данных
Программа должна вывести True, если введенная скобочная последовательность является правильной, или False в противном случае.
"""


def is_correct_bracket_sequence(sequence):
    count = 0
    for char in sequence:
        count = count + 1 if char == '(' else count - 1
        if count < 0:
            return False
    return count == 0


print(is_correct_bracket_sequence(input()))
