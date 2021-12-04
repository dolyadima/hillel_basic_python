# name: str = 'Neo'
# print(id(name))
#
#
# def namespace():  # имя функций тоже заноситься в пространство имен но выше
#     """
#     Пространство имен это словарь с именами и значениями.
#     Вместе с определением пространсва имен python соответсвенно
#     определяет и области видимости.
#     """
#
#     print(locals())  # Локальное пространство имен
#     name: str = 'Trinity'
#     print(id(name))
#     print(locals())
#     age = 50
#     print('Function namgespace():', locals())
#
#
# namespace()
# print('External namespace', locals())

# product = 'bread'  # Global variables
# print(f'GLOBAL: {product=}')
#
# def changing_product():
#     product = 'Milk'
#     print(f'LOCAL in CHANGING: {product=}')
#
#     def showing_enclosed():
#         product = 'Cola'
#         print(f'LOCAL in SHOWING: {product}')
#
#     showing_enclosed()
#     print(f'LOCAL in CHANGING: {product}')
#
#
# changing_product()
# print(f'GLOBAL: {product}')


# def wrapper():
#     def printing_age():
#         return 33
#     return printing_age
#
#
# wrapper()
#
# print(wrapper())
#
# s = wrapper()
#
# print(s)
#
# s = wrapper
#
# print(s)
#
# print(s())


def decorator():
    def wrapper(func_my):
        result = func_my()
        return result
    return wrapper


def foo():
    return 25


x = decorator()
print(x(foo))
