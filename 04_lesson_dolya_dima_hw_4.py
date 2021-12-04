num_task = 1
#
# TASK 1
#
print(f'\n----------TASK {num_task}----------\n')
input_string: str = 'предоставленная строка'
if len(input_string) < 2:
    print('Ваша строка слишком короткая - "%s"' % input_string)
else:
    print(input_string[:2] + input_string[-2:])
num_task += 1

#
# TASK 2
#
print(f'\n----------TASK {num_task}----------\n')
input_string: str = 'Hillel school top'
unique_chars: list = list()
result_chars_count: dict = dict()
for char in input_string:
    if char not in unique_chars:
        unique_chars.append(char)
        result_chars_count[char] = input_string.count(char)

print(result_chars_count)
num_task += 1

#
# TASK 3
#
print(f'\n----------TASK {num_task}----------\n')
input_data: list = ['bread', 'milk', 'kolbasa', 'buterbrod']
max_element: str = ''
max_len: int = 0
for i in input_data:
    if len(i) > max_len:
        max_len = len(i)
        max_element = i

print('Самое длинное название продукта {0} длинна {1} символов'.format(
    max_element, max_len))
num_task += 1

#
# TASK 4
#
print(f'\n----------TASK {num_task}----------\n')
input_name: str = input('Enter your name (Name): ')
print('Upper: {}\nLower: {}'.format(input_name.upper(), input_name.lower()))
num_task += 1

#
# TASK 5
#
print(f'\n----------TASK {num_task}----------\n')
input_data: str = input('Входные данные (red, red, blue, blue, black): ')
result: list = input_data.replace(',', '').split()
result: list = list(set(result))
result.sort()
print(result)
num_task += 1

#
# TASK 6
#
print(f'\n----------TASK {num_task}----------\n')
input_data: tuple = (1, 2, 3)
result: tuple = input_data[:2]
print(result)
num_task += 1

#
# TASK 7
#
print(f'\n----------TASK {num_task}----------\n')
list_of_tuples: list = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4)]
list_of_lists: list = list()
for i in list_of_tuples:
    list_of_lists.append(list(i))

print(list_of_lists)
num_task += 1

#
# TASK 8
#
print(f'\n----------TASK {num_task}----------\n')
range_list: list = list(range(-99, 99, 3))
for i in range_list:
    if i % 3 == 0:
        print(f'это <<{i}>> делится без остатка на 3')
num_task += 1

#
# TASK 9
#
print(f'\n----------TASK {num_task}----------\n')
list_1: list = [1, 2, 3, 'qwe', 'asd', [7, 8, 9]]
list_2: list = [7, 2, 9, 'qwe', 'zxc', [7, 8, 9], [12, 13, 14]]
for i in list_1:
    if i in list_2:
        print(True)
        break
