#
# TASK 1
#
# years_old: int = int(input('How old are you? '))
# if years_old == 18:
#     print('Wait a little bit')
# elif years_old > 18:
#     print('You are welcome')
# else:
#     print('Go back to school')

#
# TASK 2
#
# print('Привет python-разработчик!', end='\n')
# nickname: str = input('Введите "никнейм" [А-Яа-яA-Za-z]: ')
# gender: str = input('Введите "пол" [М/Ж]: ')
# age: int = int(input('Введите "возраст" [0-9]: '))
#
# if nickname == 'admin':
#     print('Привет, повелитель!')
#
# if (10 < age < 14 and gender == 'М') or (age > 30 and gender == 'М'):
#     print(nickname, 'советую Вам посмотреть "StarWars" или "Мандалорец"',
#           sep=', ', end='\n')
# elif 22 < age < 32 and gender == 'Ж':
#     print(nickname, 'советую Вам посмотреть "Трансформеры"',
#           sep=', ', end='\n')
# elif age < 16 and gender == 'Ж':
#     print(nickname, 'советую Вам посмотреть "Инсургент"', sep=', ', end='\n')
# elif nickname == 'Женя':
#     print(nickname, 'советую Вам посмотреть "TENET"', sep=', ', end='\n')
# elif age < 11 and gender == 'М':
#     print(nickname, 'советую Вам посмотреть "TMNT"', sep=', ', end='\n')
#
# if nickname == 'Guido':
#     print(nickname, 'огромное спасибо!', sep=', ', end='\n')

#
# TASK 3
#
# some_text: str = '(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$'
# print(some_text[::5])

#
# TASK 4
#
# input_data: str = input('количество_земных_дней, количество_часов: ')
#
# list_of_days_and_hours: list = input_data.replace(',', '').split()
# earth_days: int = int(list_of_days_and_hours[0])
# hours: int = int(list_of_days_and_hours[1])
#
# number_of_sol: float = (earth_days + hours / 24) * 1.02595675
# print('Число солов:', round(number_of_sol, 2))

#
# TASK 5
#
# big_text: str = input('Ваш большой текст: ')
# big_text = big_text.lower()
#
# if big_text[0:5] == 'черт ':
#     big_text = '#### ' + big_text[5:]
#
# if big_text[-5:] == ' черт':
#     big_text = big_text[:len(big_text)-5] + ' ####'
#
# print('Ваш большой текст: ', big_text.replace(' черт ', ' #### '), sep='')
