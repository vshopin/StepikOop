"""Артур владеет небольшой коллекцией карточек с покемонами, среди которых встречаются дубликаты. Он хочет оставить
по одной карточке каждого типа, а остальные продать.
Напишите программу, которая определяет, сколько дубликатов из своей коллекции Артур может продать.
Формат входных данных На вход программе подается произвольное количество строк, которые представляют коллекцию
карточек с покемонами. В каждой строке указывается имя покемона с карточки.
Формат выходных данных Программа должна вывести единственное число — количество карточек, которые из данной коллекции
можно продать, чтобы оставить по одной карточке каждого типа."""

import sys

data_list = [line.strip() for line in sys.stdin]
result = len(data_list) - len(set(data_list))
print(result)
