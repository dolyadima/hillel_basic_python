#
# TASK 4 (hard 4/4) v1.0
#
class Exchanger:

    def __init__(self, file_path: str):
        self._file_path: str = file_path
        self._currency_data: dict = {}

    def read_data(self):
        file = open(self._file_path, 'r')
        for i in file.read().splitlines():
            tmp: list = i.split(',')
            name: str = tmp[0]
            rate: float = float(tmp[1].split(':')[1])
            available: float = float(tmp[2].split(':')[1])
            self._currency_data[name] = {'RATE': rate, 'AVAILABLE': available}
        file.close()

    def write_data(self):
        file = open(self._file_path, 'w')
        for name_cy in self._currency_data.keys():
            file.write(f'{name_cy},'
                       f'RATE:{self._currency_data[name_cy]["RATE"]},'
                       f'AVAILABLE:{self._currency_data[name_cy]["AVAILABLE"]}\n')
        file.close()

    def get_currency_info(self, name_cy: str = 'USD'):
        if name_cy in self._currency_data.keys():
            return f'RATE {self._currency_data[name_cy]["RATE"]}, ' \
                   f'AVAILABLE {self._currency_data[name_cy]["AVAILABLE"]}\n'
        else:
            return f'INVALID CURRENCY {name_cy}\n'

    def make_exchange(self):
        # TODO write code to exchange 1
        pass

    @staticmethod
    def invalid_input():
        print('INVALID INPUT\n')


if __name__ == '__main__':
    exchanger1 = Exchanger(r'./currency_data_03.txt')
    while True:
        user_input: str = input(f'COMMAND?\n').upper()
        command: list = user_input.split()

        if len(command) == 0:
            exchanger1.invalid_input()

        if command[0] == 'COURSE':
            try:
                exchanger1.read_data()
                print(exchanger1.get_currency_info(command[1]))
            except IndexError:
                exchanger1.invalid_input()
        elif command[0] == 'EXCHANGE':
            # TODO write code to exchange 2
            pass
        elif command[0] == 'STOP':
            print(f'SERVICE STOPPED\n')
            break
        else:
            exchanger1.invalid_input()
