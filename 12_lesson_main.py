# from functools import reduce
#
# letters = ["P", "Y", "T", "H", "O", "N"]
# word = reduce(lambda x, y: x + y, letters, 'language')  # TODO: Debug me all please!
# print(word)


# class Counter:
#     def __new__(cls):
#         obj = super(Counter, cls).__new__(cls)
#         if not hasattr(cls, 'objects_list'):
#             cls.objects_list = []
#         cls.objects_list.append(obj)
#         return obj
#
#
# c1 = Counter()
# c2 = Counter()
# c3 = Counter()
# print(c1.objects_list)
