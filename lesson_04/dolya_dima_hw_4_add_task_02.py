# main list of data
data: list = [
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', ''],
    ['', '', '', '', '']
]

# lengths cells of table, to fill blank spaces
column_lengths: list = [1, 1, 1, 1, 1]

# choice of user
choice: str = '3'

# main cycle
while choice != '0':
    if choice == '1':
        coordinates: str = input('Введите x и y в формате x=2;y=2;value="v" ')
        row: int = int(coordinates[2:3])
        col: int = int(coordinates[6:7])
        val: str = coordinates[15:-1]
        if data[4 - row][col] == '':
            data[4 - row][col] = val
            print('Запись сделана!')
        else:
            rewrite: str = input('''
Ячейка занята! Перезаписать?
1) Да.
2) НЕТ!
Выбор 1-2: ''')
            if rewrite == '1':
                data[4 - row][col] = val
                print('Запись сделана!')
    elif choice == '2':
        coordinates: str = input('Введите x и y в формате x=2;y=2; ')
        row: int = int(coordinates[2:3])
        col: int = int(coordinates[6:7])
        if data[4 - row][col] == '':
            print('"пустая ячейка"')
        else:
            print(f'Значение в этой ячейке: "{data[4 - row][col]}"')
    elif choice == '3':
        # calculate lengths cells
        for i in range(5):
            column_lengths[i] = len(data[0][i]) if len(data[0][i]) > 0 else 1
            for k in range(1, 5):
                if len(data[k][i]) > column_lengths[i]:
                    column_lengths[i] = len(data[k][i])

        # flag which type of line print separate-line or data-line
        flag_line: bool = True

        # part of Y-axis
        print('Y')

        for i in range(11):
            if flag_line:  # separate-line '+--+---+----+-+---+'
                print('| ', sep='', end='')  # part of Y-axis
                for v in range(5):
                    print('+', '-' * column_lengths[v], sep='', end='')
                print('+\n', sep='', end='')
                flag_line = not flag_line
            else:  # data-line '|qq|ww |asda|a  |sss|'
                index: int = int((i - 1) / 2)  # reverse index
                print(f'{str(4 - index)} ', sep='', end='')  # index Y-axis
                for v in range(5):
                    print('|', data[index][v],
                          ' ' * (column_lengths[v] - len(data[index][v])),
                          sep='', end='')
                print('|\n', sep='', end='')
                flag_line = not flag_line
        # X-axis
        print('  -0-1-2-3-4-X')
    elif choice == '4':
        coordinates: str = input('Введите x и y в формате x=2;y=2; ')
        row: int = int(coordinates[2:3])
        col: int = int(coordinates[6:7])
        data[4-row][col] = ''
        print(f'Запись "{coordinates}" удалена!')

    # welcome text, enter number 0-4
    choice = input('''
Выбери действие:
1) Сделать запись;
2) Получить значение по координатам;
3) Показать все ячейки;
4) Удалить значение по координатам;
0) Программа завершает работу.
Выбор 0-4: ''')
