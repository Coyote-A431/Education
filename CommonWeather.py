import pyowm
import datetime
import psycopg2
import json
import pandas
import sys
import configparser


with open('settings.ini', 'r') as reader:
    api_key_line = reader.readlines()[8]

api_key_splitted_line = api_key_line.split('=')
api_key_with_spaces = api_key_splitted_line[1]
api_key = api_key_with_spaces.strip()

# api_key_s = '77fbcf5606ca03b7c831fa07e8d6f1c1'     #your API Key here as string
owm = pyowm.OWM(api_key).weather_manager()         # Use API key to get data

def print_weather(data):
    ref_time = datetime.datetime.fromtimestamp(data.ref_time).strftime('%Y-%m-%d %H:%M')
    # print(f"City\t\t: {data}")
    print(f"Time\t\t: {ref_time}")
    # print(f"Overview\t: {data.detailed_status}")
    # print(f"Wind Speed\t: {data.wind()}")
    # print(f"Humidity\t: {data.humidity}")
    print(f"Temperature\t: {data.temperature('celsius')}")
    # print(f"Rain\t\t: {data.rain}")
    print("\n")
    list = []
    list.append(ref_time)
    list.append(data.temperature('celsius'))
    return list

def get_current_weather():
    weather_api = owm.weather_at_place('Tbilisi,,GE')  # give where you need to see the weather
    weather_data = weather_api.weather          # get out data in the mentioned location

    print("***Current Weather***")
    print_weather(weather_data)
    print("\n")

def get_forecast_weather():
    dict = {'time': [], 'temp_min': [], 'temp_max': []}
    print("***5 day forecast Weather***")
    json_file = pandas.read_json('city.list.json')
    full_dict = json_file[['name', 'state', 'country']].to_numpy()
    for i in full_dict:
        current_city = ','.join(i)
        print(current_city)
        for item in owm.forecast_at_place(current_city, '3h').forecast:
            x = print_weather(item)
            time = x[0]
            temp_min = x[1]['temp_min']
            temp_max = x[1]['temp_max']
            # print(temp_min)
            for k, v in dict.items():
                if k == 'time':
                    v.append(time)
                elif k == 'temp_min':
                    v.append(temp_min)
                else:
                    v.append(temp_max)
            print(dict)

# if __name__ == '__main__':
#     get_current_weather()
#     get_forecast_weather()



# try:
#     connection = psycopg2.connect(user='postgres',
#                                   password='j27v11k96',
#                                   host='localhost',
#                                   port='5432',
#                                   database='postgres',
#                                   )
#     cursor = connection.cursor()
#     insert_query = """insert into eugene.city_weather (city, state_code, country_code, dttm, temp_min, temp_max)
#                         values (%s, %s, %s, %s, %s, %s)"""
#     t_time = datetime.datetime.now()
#     weather_data_dict = {'city': 'city_test', 'state': 'state_test', 'country': 'country_test',
#                          'time': ['2023-04-18 13:00', '2023-04-18 10:00'],
#                          'temp_min': [20.97, 23.55],
#                          'temp_max': [20.97, 23.55]}
#     df = pandas.DataFrame(data=weather_data_dict)
#     # print(df)
#     for index, row in df.iterrows():
#         cursor.execute(insert_query, (row['city'], row['state'], row['country'], row['time'], row['temp_min'], row['temp_max']))
#     connection.commit()
# except Exception as err:
#     print(err)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()


# f = pandas.read_json('city.list.json')
# full_dict = f[['name', 'state', 'country']].to_numpy()
# for i in full_dict:
#     city_info_join = ','.join(i)
#     city_info_list = city_info_join.split(',')
#     city = city_info_list[0]
#     state = city_info_list[1]
#     country = city_info_list[2]
#     print(city)
#     if state == '':
#         print(None)
#     else:
#         print(state)
#     print(country)
#     city = full_dict[i][0]
#     print(city)
#     state = full_dict[i][1]
#     if state == '':
#         print(None)
#     else:
#         print(state)
    # country = full_dict[2]
    # print(country)
    # print(','.join(i))


# stdin_fileno = sys.stdin
# for line in stdin_fileno:
#     if 'exit' == line.strip():
#         print('Found exit. Terminating the program')
#         exit(0)
#     else:
#         print('Message from sys.stdin: ---> {} <---'.format(line))

# config = configparser.ConfigParser()
# config.read('settings.ini')
# print(config.get('LOGGING', 'log_level'))
# print(config['LOGGING']['log_level'])


# d = {'time': [], 'temp_min': [], 'temp_max': []}
# for k, v in d.items():
#     if k == 'time':
#         v.append('01/01/2023')
#     elif k == 'temp_min':
#         v.append(15)
#     else:
#         v.append(20)
# print(d)

# weather_data_dict = {'city': 'city_test', 'state': 'state_test', 'country': 'country_test',
#                          'time': ['2023-04-18 13:00', '2023-04-18 10:00'],
#                          'temp_min': [20.97, 23.55],
#                          'temp_max': [20.97, 23.55]}
# df = pandas.DataFrame(data=weather_data_dict)
# print(df)

