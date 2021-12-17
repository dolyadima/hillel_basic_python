#
# TASK 0 Изи уровень 1.a,b
#
# a: list = []
# b: list = a
# a.append('asdf')
#
#
# def one():
#     x: list = ['one', 'two']
#
#     def inner():
#         print(x)
#         print(id(x))
#     return inner
#
#
# o = one()
# print(o)
# print(o())
# print(dir(o))
# print(o.__closure__)
# print(o.__closure__[0])
# print(dir(o.__closure__[0]))
# print(o.__closure__[0].cell_contents)
# a = o.__closure__[0].cell_contents
# print(id(a))
#
# a.append('asdf')
# print(o())

#
# TASK 1
#
# def user_telephone(code: str):
#     def inner(number: str):
#         return code + number
#     return inner
#
#
# my_number = user_telephone('+044')
# print(my_number('838372893'))

#
# TASK 2
#
# def methods_amount(func1):
#     def inner(my_obj: object):
#         res = func1(my_obj)
#         print(len(res))
#     return inner
#
#
# @methods_amount
# def print_all_non_magic_methods(py_obj):
#     """__init__,__str__, __add__, __hash__, etc
#     все методы, имя которых начинается и заканчивается двумя
#     нижними подчеркиваниями, называются "магическими методами",
#     так как имеют определенное назначение"""
#     methods: list = [i for i in dir(py_obj) if '__' not in i]
#     print(methods)
#     return methods
#
#
# print_all_non_magic_methods('qwe')
# print_all_non_magic_methods({1, })
# print_all_non_magic_methods(('one', 'two'))

#
# TASK 3
#
# def add_text(text: str):
#     def methods_amount(func1):
#         def inner(my_obj: object):
#             res = func1(my_obj)
#             print(text, len(res))
#         return inner
#     return methods_amount
#
#
# @add_text('need to learn')
# def print_all_non_magic_methods(py_obj):
#     methods: list = [i for i in dir(py_obj) if '__' not in i]
#     print(methods)
#     return methods
#
#
# print_all_non_magic_methods('asd')
# print_all_non_magic_methods({2, })
# print_all_non_magic_methods(('three', 'four'))

#
# TASK 4
#
"""
в задании: получаем только хэшируемые элементы, значит без проверок
поэтому можно просто hash(tuple())

а вот так можно бы было попадать в if при проверке __hash__ в dir()
items = [1, 0.1, 'ab', (2, 3), {'a': 1}, [1, 2], {2, 4}, None]
for i in items:
    if i.__hash__:
        print(i, type(i), 'is Hashable')
    else:
        print(i, type(i), 'is NO-hashable!')
"""
# cache: dict = {}
#
#
# def decorator(func):
#     def wrapper(*arg_s):
#         if hash(arg_s) not in cache.keys():  # new key, this hash not in dict
#             cache[hash(arg_s)] = func(arg_s)
#         return cache[hash(arg_s)]  # return anyway
#     return wrapper
#
#
# @decorator
# def some_func(*args):
#     return 'args=' + (str(args) * 3).replace(',', '').replace(' ', '')
#
#
"""
при дебаге видно, что мы не заходим в if, когда уже есть такой key[hash]
"""
# print(some_func(1, 2.2, 'pink', (1, 2), frozenset([4, 5.5, 'text'])))  # new
# print(some_func(frozenset([7, 8.8, 'mars']), 0, 1.1, 'eye', (3, 4)))  # new
# print(some_func(1, 2.2, 'pink', (1, 2), frozenset([4, 5.5, 'text'])))  # cache
# print(some_func(frozenset([7, 8.8, 'mars']), 0, 1.1, 'eye', (3, 4)))  # cache

#
# TASK 5
#
"""
вроде как везде типизирую ;)
"""
