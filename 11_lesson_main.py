# def take_letter(obj, number):
#     print('before error')
#     try:
#         letter = obj[number]
#         return letter
#     except IndexError as e:
#         print(e)
#     print('after error')
#
#
# word = 'try this Elon'
#
# print(take_letter(word, 15))


# def my_func(a, b):
#     print('Start program')
#     try:
#         c = a / b
#         return c
#     except ZeroDivisionError as e:
#         print('Error division:', e)
#     finally:
#         print('End of program')
#
#
# my_func(5, 0)


# def func1():
#     raise ZeroDivisionError
#
#
# try:
#     func1()
# except ZeroDivisionError as e:
#     print(f'Error division by zero:"{e}"')


# def func2():
#     return 10
#
#
# try:
#     assert func2() == 11, '10 not equal 11'
# except AssertionError:
#     print('Assert Error')


# my_list: list = [1, 2, 3]
# list_iter = iter(my_list)
# list_iter = my_list.__iter__()
# list_iter.__next__()


# def yield_example():
#     yield 1
#     yield 2
#     yield 3
#
#
# ye = yield_example()
# print(dir(ye))
#
# print(ye.__next__())
# print(ye.__next__())
# print(ye.__next__())
# # print(ye.__next__())  # Exception: StopIteration


# x = (i**2 for i in range(10))
# x.__next__()
