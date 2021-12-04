# 1) Зачем нужны break и continue?
# break - выйти из цикла полностью (вложенность 1)
# continue - пропустить часть цикла, след. итерация

# 2) Для каких целей следует использовать while,
# когда неизвестно кол-во элементов, делать пока выполняется какое-то условие

# а для каких for ... in ... ?
# когда известно кол-во элементов, четкое кол-во итераций/шагов

# 3) Что такое pass?
# оператор-заглушка, когда не требуются операции, например когда только создаём
# проект и описываем структуру из модулей, но пока что без реализации

# 4) Чем отличаются list от tuple?
# tuple неизменяемый

# 5) Области видимости. Классификация.
# LEGB local enclosing global built-in

# 6) Как работает функции min и max со строками?
# сравнивает в алфавитном порядке
# x: list = ['a', 'b', 'c', 'd']
# print(min(x))  # 'a'
# print(max(x))  # 'd'

# 7) В python почти все это объекты. Функция тоже?
# да, функция тоже объект

# 8) Каким образом передаются аргументы в функцию? (2 варианта)
# позиционные, именованные / a, b, c=None, *args, **kwargs

# 9) Что такое Pep?
# стандарт/протокол/набор правил, по написанию и оформлению кода
# (грубо говоря общий стандарт/договорённость)

# 10)Что такое анонимные функции?
# lambda, функция одной строчкой, без return

# 11) Зачем нужен оператор * (не про умножение)
# распаковка

# 12)Зачем нужны ключевые слова global и nonlocal?
# global для использования/изменения глобальной переменной внутри своей функции
# nonlocal чтобы вложенная функция использовала переменную внешней функции,
# но не делала её глобальной

# 13)Что такое хеш?
# уникальное значение, можно использовать только хэшируемые(неизменяемые) типы

# Какие базовые типы данных хэшируемые, а какие нет?
# int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes
# все остальные не-хэшируемые

# 14)Что может быть ключом в словаре?
# хэшируемый тип данных (всё что выше в вопросе)

# 15) напиши кратчайшее решение такой задачи:
# - в словаре поменять местами ключи и значения
# z = {1: 'a', 2: 'b', 3: 'c'}
# print(dict([(v, k) for k, v in z.items()]))
#
# - сгенерировать матрицу 5х5
# print([['']*5 for i in range(5)])
#
# - получить уникальные значения из списка
# l = [1, 1, 2, 2, 3, 3]
# print(set(l))

# 16) Какие есть способы объявления строк?
# s1: str = str(123)
# s2: str = '456'
# s3: str = "789"
# s4: str = """qwe123asd"""
# print(s1, s2, s3, s4)

# 17) Как перевернуть строку?
# print('abcdfeg'[::-1])

# 18) Приведите пример модификации списка
# list1: list = [1, 'a', [2, 'asd']]
# list1[1] = 5
# list1.append((7, 8))
# print(list1)

# 19) Как скопировать последовательность с помощью среза?
# collection1: list = ['z', 'q', 'c', 1, 2, 3]
# collection2: list = collection1[:]
# print(collection2)
#
# Как скопировать без среза?
# collection3: list = ['z', 'q', 'c', 1, 2, 3]
# collection4: list = collection3.copy()
# print(collection4)

# 20)Как получить перевернутую последовательность с помощью среза?
# my_list: list = [1, 'a', 2, 'b']
# print(my_list[::-1])

# 21) Как получить все ключи из словаря? Все значения?
# dict1: dict = {1: 'a', 2: 'b', 3: 'c'}
# print(dict1.keys(), dict1.values())
#
# Список с кортежами в которых находятся пары ключ, значение
# dict2: dict = {1: 'a', 2: 'b', 3: 'c'}
# print([(k, v) for k, v in dict2.items()])

# 22) Какие есть способы форматирования строк?
# print('string "%s" digit "%d"' % ('qwe', 123))
# print('text: {0} some: {1}'.format('qwe', 'asd'))
# test1: int = 123
# print(f'another {test1=}')
#
# Напишите результаты выражений и
# объясните почему именно такие результаты.
# x0 = 200
# y0 = x0
# print(x0 is y0)  # True, проверяем ссылки
# print(x0 == y0)  # True, проверяем значения
# print(id(x0), id(y0))
# # в Y поместили ссылку куда ссылается X
#
# # ----------
# x1 = 200
# y1 = 200
# print(x1 is y1)  # True, проверяем ссылки
# print(x1 == y1)  # True, проверяем значения
# print(id(x1), id(y1))
# # в области памяти создается ОДИН объект 200, и на него создаётся ссылка
#
# # ----------
# x2 = 2000
# y2 = 2000
# print(x2 is y2)  # True, проверяем ссылки
# print(x2 == y2)  # True, проверяем значения
# print(id(x2), id(y2))
# # в области памяти создается ОДИН объект 2000, и на него создаётся ссылка
