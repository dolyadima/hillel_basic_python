def no_return1():
    pass


def no_return2():
    ...


def custom_print(text):
    print(text * 3)


def multiply(a, b):
    return a * b


def find_ch_in_str(ch, st):
    if ch in st:
        return True
    else:
        return False


def draw_triangle():
    print(f'*        ')
    print(f'* *      ')
    print(f'*   *    ')
    print(f'*     *  ')
    print(f'*       *')
    print(f'*     *  ')
    print(f'*   *    ')
    print(f'* *      ')
    print(f'*        ')


def pass_gen(pswd, salt):
    return hash(pswd+salt)


# no_return1()
# no_return2()
# custom_print('my_text ')
# print(multiply(3, 5))
# print(find_ch_in_str('h', 'hello'))
# draw_triangle()
# print(pass_gen('qwerty1234', 'ua'))
