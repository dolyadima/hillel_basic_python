import requests


BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'


def get_temp_n_pres(city: str = 'Kharkov'):

    result: str = ''
    complete_url: str = BASE_URL + 'appid=' + API_KEY + '&q=' + city
    response = requests.get(complete_url)
    r_data: dict = response.json()
    print(r_data)
    if r_data['cod'] != '404':
        y = r_data['main']
        current_t = y['temp']
        current_p = y['pressure']
        # z = r_data['weather']
        # weather_description = z[0]['description']
        result = str((round(current_t - 273.15))) + ' ' + str(current_p)
    else:
        result = 'City not found.'

    return result


if __name__ == '__main__':
    print(get_temp_n_pres())
    # print(get_temp_n_pres('London'))
    # print(get_temp_n_pres('Cuba'))
