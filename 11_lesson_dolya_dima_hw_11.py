import os
#
# TASK 1
#
"""прочёл главу"""

#
# TASK 2
#
# try:
#     a = 1 + 'b'
# except TypeError:
#     print(f'(TypeError) Don\'t add to int string! Низя')
#
# try:
#     name1 = 'Mark'
#     name2 = name1[10]
# except IndexError:
#     print(f'(IndexError) You are out of bounds indices! Тож низя')
# finally:
#     print(f'А это выведет в любом случае...')
#
# try:
#     raise KeyError
# except KeyError:
#     print(f'(KeyError) Not a real exception!')
#
#
# def func1():
#     return 8
#
#
# try:
#     assert func1() == 7, 'Not equal 8...'
# except AssertionError as e:
#     print('Assert Error:', e)

#
# TASK 3
#
# def some_func(a, b):
#     return a / b
#
#
# try:
#     print(some_func(5, 0))
#     # raise IndexError
# except ZeroDivisionError:
#     print(f'ай яй яй делить на ноль можно не многим')
# except Exception as e:
#     print(f'Text error: {e=}')
# finally:
#     print(f'I \'am happy that you learn python')

#
# TASK 4
#
"""скрины приатачил"""

#
# TASK 5
#
"""
всё ясно
в двух словах:

есть 1 класс, хранит свою коллекцию элементов (по
умолчанию список, а так принимает Any тип), реализовно 2 метода итератора,
для прямого и обратного порядка (для этого вызывается явно reverse True),
и метод добавления элемента в коллекцию;

есть 2 класс, при инициализации хранит в себе коллекцию, направление, и
позицию 0 если прямой порядок сначала, и -1 если с конца коллекции, метод 
next пытается с помощью try получить след. элемент и пока не поднимается 
исключение о что нет такого индекса Index Error - возвращает элемент, а в
случае исключения - поднимает исключение о остановке (можно ещё делать return - 
я читал это "более питонно");

далее вызываем join который в первом случае сам вызовет магический __iter__
и будет получать элементы с помощью __next__ по умолчанию в прямом порядке,
во втором случае join-у явно передаём reverse итератор, который отдаёт 
элементы с помощью __next__ в обратном порядке

очень понятный пример итераторов ;)
"""

#
# TASK 6
#
#
#
# def example1():
#     for i in range(3):
#         x = int(input("enter a number: "))        # x: int =
#         y = int(input("enter another number: "))  # y: int =
#         print(x, '/', y, '=', x / y)
#
#
# def example2(L):  # L: list, имя совпадает с глобальной переменной
#     print("\n\nExample 2")
#     sum = 0  # нигде не используется, лишняя
#     sumOfPairs = []  # название переменной как название класса
#     for i in range(len(L)):  # можно len(L)-1 использовать, ошибки не будет, но вот логика этой функции...
#     # for i in range(len(L)-1):
#         sumOfPairs.append(L[i] + L[i + 1])
#
#     print("sumOfPairs = ", sumOfPairs)
#
#
# def printUpperFile(fileName):  # имя функции и аргумента как название класса, лучше так не делать
#     file = open(fileName, "r")
#     for line in file:
#         print(line.upper())
#     file.close()
#
#
# # мой пример функции
# def print_upper_file(file_name: str):
#     if os.path.isfile(file_name):
#         with open(file_name, 'r') as line:
#             [print(k) for k in [i.upper().rstrip('\n') for i in line.readlines()]]
#     else:
#         raise AttributeError
#
#
# def main():
#     try:
#         example1()
#     except (ValueError, ZeroDivisionError) as e:
#         print(f'Error: {e=}')
#
#     try:
#         L = [10, 3, 5, 6, 9, 3]  # L: list, плохое имя (не отображает предназначения списка)
#         example2(L)  # внутри функция использует так же имя L, изменить имя или тут или в функции
#         example2([10, 3, 5, 6, "NA", 3])  # str to int
#     except (IndexError, TypeError) as e:
#         print(f'Error: {e=}')
#
#     try:
#        example3([10, 3, 5, 6])  # нет такой функции
#     except NameError as e:
#         print(f'Error: {e=}')
#
#     try:
#         printUpperFile("doesNotExistYest.txt")
#         printUpperFile("./Dessssktop/misspelled.txt")
#     except (FileNotFoundError, AttributeError) as e:
#         print(f'Error: {e=}')
#
#     # мой пример считывания файла
#     try:
#         print_upper_file(r'/home/user/Desktop/misspelled.txt')
#     except (FileNotFoundError, AttributeError) as e:
#         print(f'Error: {e=}')
#
#
# main()
