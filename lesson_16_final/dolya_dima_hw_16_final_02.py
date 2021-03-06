#
# TASK 1 v1.0
#
from random import randint


class Game:
    __choices: list = ['rock', 'scissors', 'paper', 'lizard', 'spock']

    @classmethod
    def variants(cls):
        return ' '.join(cls.__choices)

    @classmethod
    def rand_choice(cls):
        return cls.__choices[randint(0, len(cls.__choices)-1)]

    @classmethod
    def who_win(cls, player_input: str):
        player_ch: str = player_input
        pc_choice: str = cls.rand_choice()
        result: str = f'Player: {player_ch}\nComputer: {pc_choice}\n'
        if (player_ch == 'rock' and pc_choice in ['scissors', 'lizard']) or\
           (player_ch == 'scissors' and pc_choice in ['lizard', 'paper']) or\
           (player_ch == 'paper' and pc_choice in ['rock', 'spock']) or\
           (player_ch == 'lizard' and pc_choice in ['paper', 'spock']) or\
           (player_ch == 'spock' and pc_choice in ['rock', 'scissors']):
            return result + f'Player WIN!'
        elif player_ch == pc_choice:
            return result + f'Choices equal. Nobody won.'
        else:
            return result + f'Computer WIN!'

    @staticmethod
    def invalid(param: str):
        return f'Invalid input "{param}"'


# if __name__ == '__main__':
#     while True:
#         user_input: str = input(f'Your choice ({Game.variants()})?\n').lower()
#         if user_input in Game.variants():
#             print(f'{Game.who_win(user_input)}')
#             while True:
#                 repeat_answer: str = input(f'Repeat (Y/N)?\n')
#                 if repeat_answer in ['Y', 'y']:
#                     break
#                 elif repeat_answer in ['N', 'n']:
#                     exit(0)
#                 else:
#                     print(Game.invalid(repeat_answer))
#         else:
#             print(Game.invalid(user_input))

#
# TASK 4 v1.2
#
"""
DEFAULT VALUES 'currency_data_03.txt':
USD,RATE:27.5,AVAILABLE:13500.98
UAH,RATE:27.3,AVAILABLE:39345.5
"""


class Exchanger:
    """ Base class for exchanger """

    def __init__(self, file_path: str):
        """Base init class"""

        self._file_path: str = file_path
        self._currency_data: dict = {}

    def read_data(self):
        with open(self._file_path, 'r') as file:
            for i in file.read().splitlines():
                tmp: list = i.split(',')
                name: str = tmp[0]
                rate: float = float(tmp[1].split(':')[1])
                available: float = float(tmp[2].split(':')[1])
                self._currency_data[name] = {'RATE': rate, 'AVAILABLE': available}

    def write_data(self):
        with open(self._file_path, 'w') as file:
            for name_cy in self._currency_data.keys():
                file.write(f'{name_cy},'
                           f'RATE:{self._currency_data[name_cy]["RATE"]},'
                           f'AVAILABLE:{self._currency_data[name_cy]["AVAILABLE"]}\n')

    def get_currency_info(self, name_cy: str = 'USD'):
        if name_cy in self._currency_data.keys():
            return f'RATE {self._currency_data[name_cy]["RATE"]}, ' \
                   f'AVAILABLE {self._currency_data[name_cy]["AVAILABLE"]}\n'
        else:
            return f'INVALID CURRENCY {name_cy}\n'

    def make_exchange(self, want_cy: str, value: float):
        if want_cy in self._currency_data.keys():
            for exist_cy in self._currency_data.keys():
                if want_cy != exist_cy:
                    if self._currency_data[want_cy]["RATE"] < self._currency_data[exist_cy]["RATE"]:
                        rate: float = 1 / self._currency_data[exist_cy]["RATE"]
                    else:
                        rate: float = self._currency_data[exist_cy]["RATE"]
                    product: float = value * rate
                    if self._currency_data[exist_cy]["AVAILABLE"] - product >= 0.0:
                        self._currency_data[exist_cy]["AVAILABLE"] -= product
                        self._currency_data[want_cy]["AVAILABLE"] += value
                        return f'{exist_cy} {product}, RATE {rate}\n'
                    else:
                        return f'UNAVAILABLE, REQUIRED BALANCE {exist_cy} {product}, AVAILABLE {self._currency_data[exist_cy]["AVAILABLE"]}\n'
        else:
            return f'INVALID CURRENCY {want_cy}\n'

    @staticmethod
    def invalid_input():
        return f'INVALID INPUT\n'


# if __name__ == '__main__':
#
#     exchanger1 = Exchanger(r'./currency_data_03.txt')
#
#     while True:
#         user_input: str = input(f'COMMAND?\n').upper()
#         command: list = user_input.split()
#
#         if len(command) == 0:
#             print(exchanger1.invalid_input())
#         elif command[0] == 'STOP':
#             print(f'SERVICE STOPPED\n')
#             break
#         elif command[0] == 'COURSE':
#             try:
#                 exchanger1.read_data()
#                 print(exchanger1.get_currency_info(command[1]))
#             except FileNotFoundError:
#                 print('File of currency not found!')
#             except IndexError:
#                 print(exchanger1.invalid_input())
#         elif command[0] == 'EXCHANGE':
#             try:
#                 exchanger1.read_data()
#                 print(exchanger1.make_exchange(command[1], float(command[2])))
#                 exchanger1.write_data()
#             except FileNotFoundError:
#                 print('File of currency not found!')
#             except IndexError:
#                 print(exchanger1.invalid_input())
#             except ValueError:
#                 print(exchanger1.invalid_input())
#         else:
#             print(exchanger1.invalid_input())
