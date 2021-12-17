import unittest
from .dolya_dima_hw_15_03 import get_temp_n_pres


class TestStringMethods(unittest.TestCase):
    """Перед запуском проверить значения и внести вторым параметром
       в тесты test_, так как температура всегда меняется..."""

    def test_equal_Kharkov(self):
        self.assertEqual(get_temp_n_pres(), '1 1010')

    def test_equal_London(self):
        self.assertEqual(get_temp_n_pres('London'), '8 1040')

    def test_not_equal_Cuba(self):
        self.assertNotEqual(get_temp_n_pres('Cuba'), '50 2022')

    def test_not_found(self):
        self.assertEqual(get_temp_n_pres('some_city'), 'City not found.')


if __name__ == '__main__':
    unittest.main()
