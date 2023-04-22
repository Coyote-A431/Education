from Settings import SettingsClass
from Weather import WeatherClass
from Database import DatabaseClass
from Logging import LoggingMixin
import datetime
import pandas
import time

class App:

    def __init__(self):
        self.settings = self.get_settings()
        self.loggin_mixin = LoggingMixin(self.settings.log(), App.__name__,
                                         datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S'),
                                         self.settings.to_file)
        self.weather = WeatherClass(self.settings.api_key())
        self.database = DatabaseClass(self.settings.database())

    def run(self):
        self.loggin_mixin.loggin()
        self.loggin_mixin.logger.info('Application is started')
        scheme_name = 'eugene'
        table_name = 'city_weather'
        is_correct_decision = False
        while not is_correct_decision:
            print('Default scheme name is ' + scheme_name,
                  'Default table name is ' + table_name,
                  'Do you want to change scheme/table name?',
                  'y/n:',
                  sep='\n')
            try:
                user_decision = input()
                if user_decision == 'y':
                    print('Choose number of option you want to change',
                          '1: Scheme',
                          '2: Table',
                          '3: Exit',
                          sep='\n')
                    user_point_input = input()
                    if user_point_input == '1':
                        print('Enter your scheme name:')
                        user_new_scheme_name = input()
                        scheme_name = user_new_scheme_name
                        is_correct_decision = True
                    elif user_point_input == '2':
                        print('Enter your table name:')
                        user_new_table_name = input()
                        table_name = user_new_table_name
                        is_correct_decision = True
                    elif user_point_input == '3':
                        is_correct_decision = True
                elif user_decision == 'n':
                    is_correct_decision = True
                else:
                    raise ValueError
            except ValueError:
                self.loggin_mixin.logger.info('Incorrect user input')
                print('Your input must be yes (y) or no (n)')
        self.loggin_mixin.logger.info(f"Scheme is {scheme_name}, table is {table_name}")
        json_file = pandas.read_json('city.list.json')
        self.loggin_mixin.logger.info('json file open successfully')
        full_list = json_file[['name', 'state', 'country']].to_numpy()
        for i in full_list:
            count_check_tries = 0
            is_right_try = False
            while not is_right_try:
                try:
                    city_info_join = ','.join(i)
                    weather_data_dict = self.weather.get_forecast_weather(city_info_join)
                    self.database.insert(weather_data_dict, scheme_name, table_name)
                    self.loggin_mixin.logger.info(f"Information of {city_info_join} was inserted successfully")
                    is_right_try = True
                except Exception as err:
                    print(err)
                    self.loggin_mixin.logger.info(f"{err} on {city_info_join}")
                    count_check_tries += 1
                    if count_check_tries > 1:
                        self.loggin_mixin.logger.info(f"{city_info_join} was skipped")
                        is_right_try = True
                    time.sleep(60)
        self.database.disconnection()
        self.loggin_mixin.logger.info('Database was closed')

    def get_settings(self):
        setting = SettingsClass()
        f = False
        while not f:
            try:
                print('Do you want to change log output from file to console?')
                h = input()
                if h == 'y':
                    setattr(setting, 'to_file', False)
                    f = True
                elif h == 'n':
                    setattr(setting, 'to_file', True)
                    f = True
            except Exception as err:
                print(err)
        return setting


if __name__ == '__main__':
    App().run()

