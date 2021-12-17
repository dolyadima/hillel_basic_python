
class Car:
    """Base class for cars"""

    weight: int = 0
    height: int = 0

    def __init__(self, brand: str = 'Subaru', color: str = 'blue',
                 cylinders: int = 1, volume: int = 1):
        """Base init class"""

        self._brand = brand
        self._color = color
        self._name = 'Our Car'
        self._cylinders = cylinders
        self._volume = volume
        self._power = 1

    def power(self):
        self._power = self._cylinders * self._volume

    @property
    def my_power(self):
        return self._power

    @my_power.setter
    def my_power(self, value: int = 1):
        self._power = value

    @my_power.deleter
    def my_power(self):
        del self._power

    def weight_update(self, new_weight: int = 0):
        self.weight = new_weight

    def height_update(self, new_height: int = 0):
        self.height = new_height

    @classmethod
    def class_weight_update(cls, value: int = 0):
        cls.weight = value

    @staticmethod
    def signal():
        return 'signal'

    def __repr__(self):
        return f'{self._name=} {id(self)=}'

    def __call__(self):
        return f'Some text from __call__'


c1 = Car()
c2 = Car()

# print(Car())
# print(c1())
#
# c1.height_update(11)
# c2.height_update(33)
#
# print(f'{c1.weight=} {c1.height=}')
# print(f'{c2.weight=} {c2.height=}')
#
# c1.class_weight_update(55)
#
# print(f'{c1.weight=} {c1.height=}')
# print(f'{c2.weight=} {c2.height=}')
#
# print(Car.signal())
# print(c1.signal())

# c1.get_power()
# print(f'GET: {c1._power=}')
# c1.set_power(77)
# print(f'SET: {c1._power=}')
# c1.del_power()
# try:
#     print(c1._power)
# except AttributeError as e:
#     print(f'DEL: {e}')

c1.power()

print(c1.my_power)  # GETTER
c1.my_power = 22  # SETTER
print(c1._power)
del c1.my_power  # DELETER
try:
    print(c1._power)
except AttributeError as e:
    print(f'DEL: {e}')
