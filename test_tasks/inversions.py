"""Задана последовательность чисел. Программа выводит количество инверсий пар чисел, при условии, что в заданной
последовательности, i < j и ai < aj. Примечание 1. Последовательностью будем считать объект, имеющий длину и
поддерживающий индексацию. Например, объекты типа list или range являются последовательностями"""


def inversions(obj):
    cnt = 0
    for i in range(len(obj)):
        for j in range(len(obj)):
            if i < j:
                if obj[i] > obj[j]:
                    cnt += 1
    return cnt


sequence = [1, 1, 1, 1, 1, 1]
print(inversions(sequence))
