# TASK 1
# def perimeter_diagonal_square(side: int):
#     return 4 * side, 2 ** 0.5 * side, side * side
#
#
# print(perimeter_diagonal_square(5))
# print(perimeter_diagonal_square(7))


# TASK 2
# def get_name_season(num_of_month: int):
#     if num_of_month < 1 or num_of_month > 12:
#         return f'! month "{num_of_month}" does not exist in our world !'
#     if num_of_month in [12, 1, 2]:
#         return 'winter'
#     if num_of_month in [3, 4, 5]:
#         return 'spring'
#     if num_of_month in [6, 7, 8]:
#         return 'summer'
#     else:
#         return 'autumn'
#
#
# print(get_name_season(-1))
# print(get_name_season(0))
# print(get_name_season(2))
# print(get_name_season(6))
# print(get_name_season(10))
# print(get_name_season(13))


# TASK 3
# def make_two_list(l1: list, l2: list):
#     if len(l1) != len(l2):
#         return '! len of list not equal !'
#     l3: list = []
#     for i in range(len(l1)):
#         l3.append(l1[i])
#         l3.append(l2[i])
#     return l3
#
#
# print(make_two_list([i for i in range(1, 5)], [i*10+i for i in range(1, 5)]))


# TASK 4
# def palindrome(text: str):
#     if text == text[::-1]:
#         return True
#     return False
#
#
# print(palindrome('ПОТОП'))
# print(palindrome('КОТ'))
