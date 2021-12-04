#
# TASK 1
#
# first: dict = {1: 10, 2: 20}
# second: dict = {3: 30, 4: 40}
# third: dict = {5: 50, 6: 60}
# fourth: dict = {7: 70, 8: 80}
# fifth: dict = {9: 90, 10: 100}
# list_of_dicts: list = [first, second, third, fourth, fifth]
# all_in_one: dict = {}
# for i in list_of_dicts:
#     all_in_one.update(i)
# print(all_in_one)

#
# TASK 2
#
"""
   1 вариант
"""
# squares: dict = {i: i**2 for i in range(11, 22, 1)}  # 1. создать
# sum_of_values: int = sum(squares.values())           # 2. просуммировать
# print(f'key: squares -> {squares}\nsum = {sum_of_values}')
"""
   2 вариант
"""
# print(sum({i: i**2 for i in range(11, 22, 1)}.values()))  # всё в одну строку

#
# TASK 3
#
# some_dict: dict = {5: 'five', 1: 'one', 4: 'four', 0: 'zero', 3: 'three'}
# some_dict_sorted: dict = dict(sorted(some_dict.items()))
# print(f'before: {some_dict}\nafter : {some_dict_sorted}')

#
# TASK 4
#
# input_dict: dict = {
#     'id1':
#         {
#             'name': 'Ruslan',
#             'class': 1,
#             'subjects': {'Math', 'Algorithms', 'English'}
#         },
#     'id2':
#         {
#             'name': 'Mark',
#             'class': 2,
#             'subjects': {'Geometry', 'Java', 'Cooking'}
#         },
#     'id3':
#         {
#             'name': 'Ruslan',
#             'class': 1,
#             'subjects': {'Math', 'Algorithms', 'English'}
#         }
# }
# new_dict: dict = {}
# for k, v in input_dict.items():
#     if v not in new_dict.values():
#         new_dict[k] = input_dict[k]
# print(f'orig: {input_dict}\nnew : {new_dict}')

#
# TASK 5
#
# list_of_dict_with_dupl: list = [
#     {"V": "S001"},
#     {"V": "S002"},
#     {"VI": "S001"},
#     {"VI": "S005"},
#     {"VII": "S005"},
#     {"V": "S009"},
#     {"VIII": "S007"}
# ]
# list_of_dict_uniq_val: list = []
# unique: set = set()
# for i in range(len(list_of_dict_with_dupl)):
#     for k, v in list_of_dict_with_dupl[i].items():
#         if v not in unique:
#             unique.add(v)
#             list_of_dict_uniq_val.append({k: v})
#
# print(f'\n{list_of_dict_with_dupl}\n{list_of_dict_uniq_val}')

#
# TASK 6
#
# английский не проблема ;)
# https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
# shedule: dict = {
#     'Monday':
#         ['clean house', 'drive car', 'meet with friends'],
#     'Tuesday':
#         None,
#     'Wednesday':
#         ['manicure', 'hammam', 'beer']
# }
# print(f'{shedule}')
"""
   1 вариант, миллион строк...
"""
# sum_of_el_lists: int = 0
# for v in shedule.values():
#     if isinstance(v, list):
#         sum_of_el_lists += len(v)
# print(sum_of_el_lists)
"""
   2 вариант, самое то
"""
# print(sum([len(i) for i in shedule.values() if isinstance(i, list)]))

#
# TASK 7
#
# dict-methods скрин теста приатачил
