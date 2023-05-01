"""
Реализуйте декоратор @jsonify, преобразующий возвращаемое значение декорируемой функции в строку формата JSON.
Также декоратор должен сохранять имя и строку документации декорируемой функции.
Примечание 1. Гарантируется, что возвращаемое значение функции принадлежит типу, который поддерживается форматом JSON.
"""

import json
import functools


def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = json.dumps(func(*args, **kwargs))
        return result

    return wrapper


@jsonify
def make_user(id, live, options):
    return {'id': id, 'live': live, 'options': options}


print(make_user(4, False, None))
