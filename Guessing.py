import random
import time
import os
import datetime
import sys
# num_to_guess = random.randint(1, 100)
# print(num_to_guess)
# user_guess = -1

# def rand_num():
#     num_to_guess = random.randint(1, 100)
#     print(num_to_guess)
#     return num_to_guess

def get_validation():
    is_valid_input = False
    while not is_valid_input:
        try:
            u_num = input('Guess the number: ')
            u_num = int(u_num)
            # is_valid_input = True
        except ValueError:
            print('You entered not number or left empty field')
        if u_num == 61:
            print('You are right!')
            is_valid_input = True
        else:
            print('Try again')
        print(u_num)
    return u_num


###


class guessing:

    def __init__(self):
        self.number_to_guess = self.rand_num()
        data_list = self.comparison()
        self.start_time = data_list[0]
        self.user_values = data_list[1]
        self.tries = data_list[2]
        self.end_time = data_list[3]
        self.filepath = self.create_logs()

    def rand_num(self):
        random_number = random.randint(1, 100)
        print(random_number)
        return random_number

    def test_func(self):
        with open(self.filepath, 'w+') as new_file:
        # start logging
            while True:
                new_file.writelines(self.comparison(self.number_to_guess), self.validation())
        # self.comparison(self.number_to_guess)

    def comparison(self, a, b):
        is_first_iteration = True
        is_valid_input = False
        previous_input = -1
        try_counter = 0
    # part with start time for log
        current_start_datetime = datetime.datetime.now()
        current_start_time = current_start_datetime.time()
        full_start_time_str = str(current_start_time)
        dot_start_time = full_start_time_str.rfind('.')
        start_time_str = full_start_time_str[:dot_start_time]
        print(start_time_str)
        user_values = []
        while not is_valid_input:
            try:
                user_num = input('Guess the number from 1 to 100: ')
                current_input = int(user_num)
                current_input_str = str(current_input)
                user_values.append(current_input_str)
                if current_input == self.number_to_guess:
                    try_counter += 1
                    print('You are great!')
                    end_datetime = time.localtime()
                    end_time = time.strftime('%H:%M:%S', end_datetime)
                    result = []
                    result.append(start_time_str)
                    try_counter_str = str(try_counter)
                    result.append(user_values)
                    result.append(try_counter_str)
                    result.append(end_time)
                    print(result)
                    is_valid_input = True
                elif current_input in range(self.number_to_guess - 10, self.number_to_guess + 11):
                    print('Very close')
                elif current_input in range(self.number_to_guess - 25, self.number_to_guess + 26)\
                        and current_input not in range(self.number_to_guess - 10, self.number_to_guess + 11):
                    print('Close')
                elif current_input in range(self.number_to_guess - 50, self.number_to_guess + 51)\
                        and current_input not in range(self.number_to_guess - 25, self.number_to_guess + 26):
                    print('Far')
                else:
                    print('Very far')
                if not is_first_iteration:
                    if previous_input != current_input:
                        if previous_input < self.number_to_guess and not is_valid_input:
                            if current_input > previous_input:
                                print('Closer')
                            else:
                                print('Further')
                        elif previous_input > self.number_to_guess and not is_valid_input:
                            if current_input > previous_input:
                                print('Further')
                            else:
                                print('Closer')
                is_first_iteration = False
                previous_input = current_input
                try_counter += 1
            except ValueError:
                print('You entered not number or left empty field')
        return result

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
        start_time_filename = self.start_time.replace(':', '.')
        log_filename = filename_without_extension + '_' + start_time_filename + '.txt'
        filepath = os.path.join(log_dir_path, log_filename)
        return filepath
        # with open(filepath, 'w+') as new_file:
        #     new_file.write('1) Start time: ' + self.start_time + '\n')
        #     new_file.write('2) User values: \n')
        #     my_list = map(lambda x: x + '\n', self.user_values)
        #     new_file.writelines(my_list)
        #     new_file.write('3) End time: ' + self.end_time + '\n')
        #     new_file.write('4) Count tries: ' + self.tries + '\n')
        #     new_file.close()


test = guessing()
# test.comparison()
test.create_logs()
