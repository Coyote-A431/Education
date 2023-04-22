import datetime
import pyowm
import pandas


class WeatherClass:

    def __init__(self, api_key):
        self.api_key = api_key
        self.owm = pyowm.OWM(api_key).weather_manager()

    def get_forecast_weather(self, city):
        data_frame_list = []
        for item in self.owm.forecast_at_place(city, '3h').forecast:
            city_info_list = city.split(',')
            current_city = city_info_list[0]
            state = city_info_list[1]
            if state == '':
                state = None
            country = city_info_list[2]
            data_frame_list.append([current_city,
                                    state,
                                    country,
                                    datetime.datetime.fromtimestamp(item.ref_time).strftime('%Y-%m-%d %H:%M'),
                                    item.temperature('celsius')['temp_min'],
                                    item.temperature('celsius')['temp_max']])
        df = pandas.DataFrame(data_frame_list, columns=[
            'city',
            'state_code',
            'country_code',
            'processed_dttm',
            'temp_min',
            'temp_max'
        ])
        return df





