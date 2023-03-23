import random
import time
import os

class Guess_Test:

    def __init__(self):
        self.filepath = self.create_logs()
        global previous_input
        global is_first_iteration
        global is_user_guess
        previous_input = -1
        is_first_iteration = True
        is_user_guess = False

    def random_number(self):
        random_number = random.randint(1, 100)
        print(random_number)
        return random_number

    def validation(self):
        user_input = input('Guess the number from 1 to 100: ')
        with open(self.filepath, 'a+') as add_user_values:
            add_user_values.write(f'[{user_input}]' + '\n')
        return user_input

    def comparison(self, current_input, number_to_guess):
        global previous_input
        global is_first_iteration
        global is_user_guess
        try:
            if current_input == number_to_guess:
                print('You are great!')
                is_user_guess = True
            elif current_input in range(number_to_guess - 10, number_to_guess + 11):
                print('Very close')
            elif current_input in range(number_to_guess - 25, number_to_guess + 26) \
                    and current_input not in range(number_to_guess - 10, number_to_guess + 11):
                print('Close')
            elif current_input in range(number_to_guess - 50, number_to_guess + 51) \
                    and current_input not in range(number_to_guess - 25, number_to_guess + 26):
                print('Far')
            else:
                print('Very far')
            if not is_first_iteration and not is_user_guess:
                if previous_input != current_input:
                    if previous_input < number_to_guess:
                        if current_input > previous_input:
                            print('Closer')
                        else:
                            print('Further')
                    elif previous_input > number_to_guess:
                        if current_input > previous_input:
                            print('Further')
                        else:
                            print('Closer')
            previous_input = current_input
            is_first_iteration = False
        except Exception as err:
            with open(self.filepath, 'a+') as err_report:
                err_report.write(str(err) + '\n')
                err_report.close()
        except KeyboardInterrupt:
            with open(self.filepath, 'a+') as err_report:
                err_report.write('User ended script' + '\n')
                err_report.close()
        return current_input

    def create_logs(self):
        path = os.path.realpath(__file__)
        index_of_last_slash = path.rfind('\\')
        path_without_filename = path[:index_of_last_slash + 1]
        dirname = 'Logs'
        log_dir_path = path_without_filename + dirname
        if not os.path.exists(log_dir_path):
            os.mkdir(dirname)
        filename = os.path.basename(path)
        filename_split = filename.split('.')
        filename_without_extension = filename_split[0]
        start_datetime = time.localtime()
        start_time = time.strftime('%H:%M:%S', start_datetime)
        start_time_filename = start_time.replace(':', '.')
        log_filename = filename_without_extension + '_' + start_time_filename + '.txt'
        filepath = os.path.join(log_dir_path, log_filename)
        with open(filepath, 'w+') as new_file:
            new_file.write('1) Start time: ' + start_time + '\n')
            new_file.close()
        return filepath

    def __function(self):
        try:
            with open(self.filepath, 'a+') as user_values:
                user_values.write('2) User values: ' + '\n')
                user_values.close()
            number_to_guess = self.random_number()
            try_counter = 0
            while not is_user_guess:
                try:
                    valid_value = self.validation()
                    user_input = int(valid_value)
                    self.comparison(user_input, number_to_guess)
                    if user_input == number_to_guess:
                        try_counter += 1
                        end_datetime = time.localtime()
                        end_time = time.strftime('%H:%M:%S', end_datetime)
                        with open(self.filepath, 'a+') as add_last_points:
                            add_last_points.write('3) End time: ' + end_time + '\n')
                            add_last_points.write('4) User tries: ' + str(try_counter) + '\n')
                            add_last_points.close()
                    try_counter += 1
                except ValueError:
                    try_counter += 1
                    print('You entered not number or left empty field')
        except Exception as err:
            with open(self.filepath, 'a+') as err_report:
                err_report.write(str(err) + '\n')
                err_report.close()
        except KeyboardInterrupt:
            with open(self.filepath, 'a+') as err_report:
                err_report.write('User ended script' + '\n')
                err_report.close()

    def function(self):
        self.__function()


test = Guess_Test()
test.function()


# test._Guess_Test__function()


