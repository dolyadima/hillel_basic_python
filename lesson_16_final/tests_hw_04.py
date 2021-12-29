import unittest
import os
from .dolya_dima_hw_16_final_02 import Exchanger, Game


class TestsInput(unittest.TestCase):
    """
    Перед запуском внести в файл 'currency_data_03.txt':
USD,RATE:27.5,AVAILABLE:13500.98
UAH,RATE:27.3,AVAILABLE:39345.5
    """

    def test_exch_course_uah(self):
        exchanger2 = Exchanger(os.path.dirname(os.path.realpath(__file__)) + '/currency_data_03.txt')
        exchanger2.read_data()
        self.assertEqual(exchanger2.get_currency_info('UAH'), 'RATE 27.3, AVAILABLE 39345.5\n')

    def test_exch_course_usd(self):
        exchanger2 = Exchanger(os.path.dirname(os.path.realpath(__file__)) + '/currency_data_03.txt')
        exchanger2.read_data()
        self.assertEqual(exchanger2.get_currency_info('UAH'), 'RATE 27.3, AVAILABLE 39345.5\n')

    def test_exch_invalid(self):
        exchanger2 = Exchanger(os.path.dirname(os.path.realpath(__file__)) + '/currency_data_03.txt')
        exchanger2.read_data()
        self.assertEqual(exchanger2.get_currency_info('BTC'), 'INVALID CURRENCY BTC\n')

    def test_game_invalid(self):
        self.assertEqual(Game.invalid('text'), 'Invalid input "text"')

    def test_game_variants(self):
        self.assertEqual(Game.variants(), 'rock scissors paper lizard spock')


if __name__ == '__main__':
    unittest.main()
