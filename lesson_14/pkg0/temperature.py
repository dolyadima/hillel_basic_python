from tests import test_function, x
# from ..pkg1.tests_from_pkg2 import super_test


def temperature():
    return 3


print(test_function(temperature, 2))
print(test_function(temperature, 3))
print(test_function(temperature, 4))
print(x)
# print(super_test())
