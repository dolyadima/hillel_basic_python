# def base_cat():
#     cat: dict = {'paws': 4}
#
#     def my_cat(name):
#         cat['name'] = name
#         return cat
#
#     return my_cat


# def cat():
#     return 'meow'
#
#
# def dog():
#     return 'woof'
#
#
# def decor_animal(func):
#
#     def wrapper():
#         answer = func()
#         if answer == 'meow':
#             return 'Cat say: ' + answer
#         elif answer == 'woof':
#             return 'Dog say: ' + answer
#     return wrapper
#
#
# print(decor_animal(cat)())


# def outer_func():
#
#     car_list = ['moskvich', 'rollseroyce', 'bentley']  # enclosing for inner_func
#
#     def inner_func():
#         print('%s and it adres %s' % (car_list, id(car_list)))
#
#     return inner_func
#
#
# outter_func_first = outer_func()
#
# print(outter_func_first())
# dir(outter_func_first)
# dir(outter_func_first.__closure__)
# dir(outter_func_first.__closure__[0].cell_contents)
# enclosing_variable = outter_func_first.__closure__[0].cell_contents
# enclosing_variable.add('niva')
#
# outter_func_first()
