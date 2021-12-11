#
# TASK 1
#
# print(f'Example 1:')
# def my_gen():
#     num: int = 1
#     print(f'First')
#     yield num
#     num += 1
#     print(f'Second')
#     yield num
#     num += 1
#     print(f'Third last')
#     yield num
#
#
# for i in my_gen():
#     print(i)
#
# print(f'\nExample 2:')
# gen = (i**2 for i in range(1, 5))
# while True:
#     try:
#         print(gen.__next__())
#     except StopIteration as e:
#         print(f'{e}')
#         break
#
# print(f'Example 3:')
#
#
# def f_gen(m):
#     b: int = 1
#     for n in range(1, m):
#         yield n**3 + b
#         b += 2
#
#
# gen = f_gen(5)
# for i in gen:
#     print(i)


#
# TASK 2, 3
#
# from functools import reduce
#
#
# def sum_of_el(x, y):
#     """Внешняя функция суммы пары элементов"""
#     return x + y
#
#
# def my_reduce(my_func, my_iterable):
#     """Своя реализация функции reduce()"""
#
#     my_iterator: iter = iter(my_iterable)  # создаю итератор итерируемого объекта
#     result = next(my_iterator)  # получаю его первый элемент
#     """
#     Если длина последовательности равна 0, то raise ошибка
#     как и в оригинальном reduce из functools, я проверял.
#     """
#
#     """
#     В цикле for у итератора вызывается метод __next__() и получаем следующий
#     элемент, до того момента пока for не получит StopIteration;
#     И передаём во внешнюю функцию два параметра, прошлое значение,
#     и следующий элемент последовательности.
#     """
#     for elem in my_iterator:
#         result = my_func(result, elem)
#     return result  # итоговый результат
#
#
# def test_reduce(func_reduce, func_my_reduce, func_lambda, data):
#     """
#     В функцию тестирования передаются:
#     - оригинальная функция reduce;
#     - самописная функция reduce;
#     - функция для пары элементов, которую передаём в reduce;
#     - итерируемый объект.
#     Первый assert сравнивает результат с оригинальным reduce-ом,
#     второй assert сравнивает с built-in функцией sum(), у меня внешняя
#     функция - сумма, так что можно её юзать для проверки.
#     Ну и для принта, если не raise ошибка во время assert - я отдаю True,
#     для наглядности.
#     """
#     assert func_reduce(func_lambda, data) == func_my_reduce(func_lambda, data), 'Not equal'
#     assert func_my_reduce(func_lambda, data) == sum(data), 'Not equal'
#     return True
#
#
# for i in range(1, 11):
#     tmp: list = list(range(i))
#     print(f'Тест {str(i).zfill(2)}. {tmp} = {test_reduce(reduce, my_reduce, sum_of_el, tmp)}')

#
# TASK 4
#
# class Class1:
#
#     val1: str = 'qwe'
#     val2: str = 'asd'
#
#     def __init__(self):
#         self.weight: int = 1
#         self.height: int = 2
#
#     def get_scope(self):
#         return vars(self)
#         # return (self.__dict__)
#         # return dir(self)
#
#
# cls1 = Class1()
# print(cls1.get_scope())
