import random
import time
import os
import traceback

class Guess_Test:

    def __init__(self):
        self.filepath = self.create_logs()

    def random_number(self):
        random_number = random.randint(1, 100)
        print(random_number)
        return random_number

    def validation(self):
        is_valid_input = False
        while not is_valid_input:
            try:
                user_input = input('Guess the number: ')
                with open(self.filepath, 'a+') as add_user_values:
                    add_user_values.write(user_input + '\n')
                current_input = int(user_input)
                is_valid_input = True
            except ValueError:
                print('You entered not number or left empty field')
        return current_input

    def comparison(self, current_input, number_to_guess):
        if current_input == number_to_guess:
            print('You are great!')
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

    def function(self):
        try:
            with open(self.filepath, 'a+') as user_values:
                user_values.write('2) User values: ' + '\n')
                user_values.close()
            number_to_guess = self.random_number()
            try_counter = 0
            is_user_guess = False
            is_first_iteration = True
            previous_input = -1
            while not is_user_guess:
                user_input = self.validation()
                self.comparison(user_input, number_to_guess)
                if user_input == number_to_guess:
                    try_counter += 1
                    end_datetime = time.localtime()
                    end_time = time.strftime('%H:%M:%S', end_datetime)
                    with open(self.filepath, 'a+') as add_last_points:
                        add_last_points.write('3) End time: ' + end_time + '\n')
                        add_last_points.write('4) User tries: ' + str(try_counter) + '\n')
                        add_last_points.close()
                    is_user_guess = True
                if not is_first_iteration:
                    if previous_input != user_input:
                        if previous_input < number_to_guess and not is_user_guess:
                            if user_input > previous_input:
                                print('Closer')
                            else:
                                print('Further')
                        elif previous_input > number_to_guess and not is_user_guess:
                            if user_input > previous_input:
                                print('Further')
                            else:
                                print('Closer')
                previous_input = user_input
                is_first_iteration = False
                try_counter += 1
        except Exception as err:
            with open(self.filepath, 'a+') as bug_report:
                bug_report.write(str(err))
                bug_report.close()


test = Guess_Test()
test.function()