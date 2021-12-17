"""
Полиморфизм — это возможность использования одного и того же
кода с разными типами аргументов и переменных
"""


# class Dog:
#     def voice(self):
#         return 'Gav'
#
#
# class Cat:
#     def voice(self):
#         return 'Meow'
#
#
# class Dove:
#     def voice(self):
#         return 'Kurlik'
#
#
# dog1 = Dog()
# cat1 = Cat()
# dove1 = Dove()
#
# l1: list = [dog1, cat1, dove1]
#
# for i in l1:
#     print(i.voice())


# import requests
#
#
# base_url = 'http://api.openweathermap.org/data/2.5/weather?'
# api_key = 'd82759ebf4a4a5ed987117c4027b9dfa'
#
#
# def get_temp_n_pres(city: str='Kharkov'):
#
#     result: str = ''
#     complete_url = base_url + 'appid=' + api_key + '&q=' + city
#     response = requests.get(complete_url)
#     r_data = response.json()
#     if r_data['cod'] != '404':
#         y = r_data['main']
#         current_t = y['temp']
#         current_p = y['pressure']
#         z = r_data['weather']
#         # weather_description = z[0]['description']
#         result = 'Celsius:' + str((round(current_t - 273.15))) + ' ' +\
#                  'Pressure:' + str(current_p)
#     else:
#         result = 'City not found.'
#
#     return result
#
#
# if __name__ == '__main__':
#     print(get_temp_n_pres())
#     print(get_temp_n_pres('London'))


# from unittest import TestCase, main
#
#
# class TestWeather(TestCase):
#     def test_city(self):
#         self.assertTrue(True)
#
#
# if __name__ == '__main__':
#     main()
