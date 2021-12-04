from datetime import datetime as dt

# tmp1 = dt.now()
# tmp2 = dt.today()
#
# print(f'{tmp1}\n{tmp2}')


# def get_year():
#     print(dt.now().year)


# get_year()


# start = dt.now()
#
#
# def wrapper():
#     def get_my_year_of_birthday(age: int):
#         print(f'Current year: {dt.now().year}\n'
#               f'Your age: {age}\n'
#               f'Year of birth: {dt.now().year - age}')
#     return get_my_year_of_birthday
#
#
# wrapper()(25)
#
# x = wrapper()
# x(25)
#
#
# def sum_of_digit(num: int = 123456789):
#     if num < 10:
#         return num
#     else:
#         return sum_of_digit(sum(map(int, list(str(num)))))
#
#
# print(sum_of_digit())
#
# x: int = 0
#
#
# def func1(z: int) -> int:
#     return z
#
#
# print(f'TIME: {dt.now() - start}')


def counting_time(function):
    def wrapper():
        start = dt.now()
        answer = function()
        print(dt.now() - start)
        return answer
    return wrapper


@counting_time
def func1():
    answer: list = [i ** 2 for i in range(100000)]
    return answer


# counting_time(func1)()
# counting_time()
func1()
