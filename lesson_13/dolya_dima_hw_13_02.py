
class Fan:
    """Base class for fans"""

    vendor_country: str = 'Ukraine'

    def __init__(self, number_of_blades: int = 3, diameter: int = 30,
                 color: str = 'white', energy: bool = False):
        """Base init class"""

        self._number_of_blades = number_of_blades
        self._diameter = diameter
        self._color = color
        self._energy = energy

    @property
    def t_power(self):  # GETTER status of energy
        return self._energy

    @t_power.setter
    def t_power(self, value: bool = False):  # SETTER set state energy
        self._energy = value
        # self._power = not self._power  # as an option, for toggle

    @t_power.deleter
    def t_power(self):
        del self._energy  # DELETER remove power option :)

    @classmethod
    def change_country_class(cls, value: str = 'Ukraine'):
        cls.vendor_country = value

    @staticmethod
    def blow():
        return 'Blow by the wind...'

    def __repr__(self):
        return f'Class Fan. Make your fan. Just do it.'

    def __call__(self):
        return f'Some text from instance class Fan.'


"""init & vars"""
fan1 = Fan()  # init
print(vars(fan1))

"""set get del"""
print(f'{fan1.t_power=}')  # get
fan1.t_power = True  # set
print(f'{fan1.t_power=}')
del fan1.t_power  # del
print(vars(fan1))

"""classmethod"""
print(fan1.vendor_country)
fan1.change_country_class('Germany')
print(fan1.vendor_country)

"""staticmethod"""
print(Fan.blow())  # class
print(fan1.blow())  # instance

"""repr call"""
print(Fan())  # __repr__
print(fan1())  # __call__
