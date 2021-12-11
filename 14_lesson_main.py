"""
   Инкапсуляция - механизм сокрытия, позволяющий разграничивать
   доступ к различным компонентам программы.
"""


class Kettle(object):
    """Kettle class describe the kettle workflow"""

    def __init__(self, water=2, real_price=0):
        self.water = water
        self._real_price = real_price  # protected variable
        self.capacity = 0
        self.__plastic_mark = 'P'
        self.__length_cable__ = 1

    def __get_length_cable__(self):
        return self.__length_cable__

    def turn_on(self):
        """Main method"""
        self._boil()

    def _check_temperature(self):
        print('I am checking water temperature')

    def _boil(self):
        print('Boiling water')

    def _noise(self):
        print('maiking noise')

    def __turn_off(self):
        print('turn off the kettle')

    def _checking_water_level(self):
        print('Ichecked')

    @property
    def water_inside(self):
        return self.water

    @water_inside.setter
    def water_inside(self, val=0):
        self.water = val

    @water_inside.deleter
    def water_inside(self):
        self.water = 0


kettle1 = Kettle()
# print(kettle1._real_price)
# print(kettle1.__plastic_mark)
# print(vars(kettle1))

print(kettle1.water_inside)
kettle1.water_inside = 100
print(kettle1.water_inside)
del kettle1.water_inside
print(kettle1.water_inside)

print(kettle1.__get_length_cable__())  # magic method for inner realisation


# class Car:
#
#     def __init__(self, marka='BMW'):
#         self.__marka = marka
#         self.power = 100
#
#     def set_power(self):
#         if self.__marka == 'BMW':
#             return 100
#         elif self.__marka == 'Mercedes':
#             return 200
#
#
# car1 = Car('Mercedes')


# class Price:
#
#     def __init__(self):
#         self.price = 'Public'
#         self._price = 'Protected'
#         self.__price = 'Private'
#
#     def get_price(self):
#         print(self.price)
#
#     def _get_price(self):
#         print(self._price)
#
#     def __get_price(self):
#         print(self.__price)
#
#
# price1 = Price()
# print(vars(price1))
# print(dir(price1))
# price1.get_price()
# price1._get_price()
# price1._Price__get_price()
