#
# TASK 1
#
"""
   1 вариант
   по типу регистрации с созданием пароля
"""
# while True:
#     first_pass: str = input('Enter pass: ')
#     second_pass: str = input('Re-type pass: ')
#     if first_pass == second_pass:
#         print('Good job! Password has been created.')
#         break
#     else:
#         print('First pass not equal second!!! Repeat.')
"""
   2 вариант
   пароль давно создан, просто ввод и проверка со старым, как при sudo ;)
"""
# pass_1: str = input('Create your pass: ')
# while True:
#     pass_2: str = input('Enter pass: ')
#     if pass_1 == pass_2:
#         print('Good job! Access granted.')
#         break
#     else:
#         print('Your password is incorrect!!! Is not allowed.')

#
# TASK 2
#
# input_list: list = ['bear', 'eg', 'milk', 'eg', 'eg', 'eg']
# word: str = 'eg'
# while word in input_list:
#     input_list.remove(word)
# print(input_list)

#
# TASK 3
#
"""
   для тестов один list закоментить / другой list раскоментить
"""
# input_list: list = [12, 22, 66, 44, 76, 534]
# # input_list: list = [11, 23, 65, 44, 76, 533]
# is_even: bool = False  # even - четный / odd - нечетный
# i = 0
# while i < len(input_list):
#     if input_list[i] % 2 != 0:
#         break
#     i += 1
# else:
#     print('all numbers are even')
#     is_even = True
#
# if not is_even:
#     print('NO')

#
# TASK 4
#
"""
   x = [1, 2, 3, [123, 456, 789]]
   y = copy.copy(x)  # возвращает поверхностную копию x. (ссылки на изменяемые объекты)
   y[3].append(4)
   print(x, y)  # [1, 2, 3, [123, 456, 789, 4]] [1, 2, 3, [123, 456, 789, 4]]

   x = [1, 2, 3, [123, 456, 789]]
   z = copy.deepcopy(x)  # возвращает полную копию x.
   z[3].append(4)
   print(x, z)  # [1, 2, 3, [123, 456, 789]] [1, 2, 3, [123, 456, 789, 4]]
"""
# [print(i) for i in dir(set) if '_' not in i]

#
# TASK 6
#
# set1: set = {1, 2, 3, 'foo', 'bar', 'baz'}
# set2: set = {7, 8, 3, 'quz', 'qwe', 'baz'}
#
# set1.add('zxc')      # add
# set1.clear()         # clear
# set1 = set2.copy()   # copy
# set1.update(set2)    # update
# set1.discard('baz')  # discard
# set1.pop()           # pop (random)
# set1.remove(8)       # remove (may be exception)
#
# set3: set = {11, 12, 13, 'foo', 'bar', 'baz'}
# set4: set = {11, 22, 33, 'quuz', 'asd', 'bar'}
#
# set5: set = set4.union({8, 9, 'pro'})        # union |
# set6: set = set4.intersection(set5)          # intersection &
# set4.intersection_update(set6)               # intersection_update
# set5: set = set3.difference(set4)            # difference -
# set3.difference_update(set4)                 # difference_update
# set7: set = set5.symmetric_difference(set6)  # symmetric_difference ^
# set5.symmetric_difference_update(set6)       # symmetric_difference_update
#
# set8: set = {1, 2, 'q'}
# set9: set = {1, 2, 'q', 'wer', 'ty'}
#
# var1: bool = set8.issubset(set9)    # 15. issubset <=
# var2: bool = set9.issuperset(set8)  # 16. issuperset >=
# var3: bool = set8.isdisjoint(set9)  # 17. isdisjoint
#
# print(f'{set1=}\n{set2=}\n{set3=}\n{set4=}\n{set5=}\n{set6=}\n'
#       f'{set7=}\n{set8=}\n{set9=}\n{var1=}\n{var2=}\n{var3=}',
#       sep='', end='')
