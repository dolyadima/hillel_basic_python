# Задача 1

# def user_telephone(first_num: str):
#     def user_telephone_full(second_num: str):
#         full_num = first_num + second_num
#         return full_num
#     return user_telephone_full
#
#
# my_number = user_telephone('+044')
#
# print(my_number('838372893'))

# Задача 2
#
# def methods_amount(func):
#     def wrapper(object_f1: object):
#         result = func(object_f1)
#         q = 0
#         for i in result:
#             q += 1
#         return q
#     return wrapper
#
# @methods_amount
# def dir_object(object_f: object):
#     dir_object_v = dir(object_f)
#     result = [x for x in dir_object_v if '_' not in x]
#     print(result)
#     return result
#
# print(dir_object('1'))
# print(methods_amount(dir_object)('1'))

# Задача 3
#
# def methods_amount(text: str):
#     def decorator(func):
#         def wrapper(object_f1: object):
#             result = func(object_f1)
#             q = 0
#             for i in result:
#                 q += 1
#             return text + ' ' + str(q)
#         return wrapper
#     return decorator
#
#
# @methods_amount('need to learn')
# def dir_object(object_f: object):
#     dir_object_v = dir(object_f)
#     result = [x for x in dir_object_v if '_' not in x]
#     print(result)
#     return result
#
# print(dir_object('1'))

# Задача 4
#
# hash_data_dict = {}
#
# def decorator(func):
#     def wrapper(**kwargs):
#         all_key: str = ''
#         dict_temp: dict = {}
#         hash_kay_tmp: int = 0
#         dict_temp = hash_data_dict.copy()
#
#         for key, value in kwargs.items():
#             all_key += str(key)+str(value)
#
#         hash_kay_tmp = hash(all_key)
#
#         if len(dict_temp.keys()) == 0:
#             hash_data_dict[hash_kay_tmp] = kwargs
#             func(**kwargs)
#         else:
#             for i in dict_temp.keys():
#                 if i == hash_kay_tmp:
#                     func(**hash_data_dict.get(i))
#                 else:
#                     hash_data_dict.update({hash_kay_tmp: kwargs})
#                     func(**kwargs)
#                     break
#     return wrapper
#
#
# @decorator
# def intro(**data):
#     value_dict = {}
#     for key, value in data.items():
#         value_dict[key] = value
#         print("{} is {}".format(key, value))
#     print('\n')
#     return value_dict
#
#
# intro(Firstname="1", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
# intro(Firstname="1", Email1="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
# intro(Firstname="2", Lastname="Wood", Email="johnwood@nomail.com", Age=25, Phone=9876543210)
# intro(Firstname="3", Lastname2="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
# intro(Firstname="4", Lastname="32423", Email="johnwood@nomail.com", Country="fdgf", Age=25, Phone=9876543210)
# intro(Firstname="5", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
# intro(Firstname="6", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=345)
# intro(Firstname="6", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=345)
# intro(Firstname="7", Lastname="sdf", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
#
# print(hash_data_dict)
