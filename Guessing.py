import random
import time
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

    def rand_num(self):
        random_number = random.randint(1, 100)
        return random_number

    def comparison(self):
        is_first_iteration = True
        is_valid_input = False
        previous_input = -1
        try_counter = 0
        begin_datetime = time.localtime()
        begin_time = time.strftime('%H:%M:%S', begin_datetime)
        print(begin_time)
        while not is_valid_input:
            try:
                user_num = input('Guess the number from 1 to 100: ')
                current_input = int(user_num)
                if current_input == self.number_to_guess:
                    print('You are great!')
                    end_datetime = time.localtime()
                    end_time = time.strftime('%H:%M:%S', end_datetime)
                    print(end_time)
                    is_valid_input = True
                elif current_input in range(self.number_to_guess - 10, self.number_to_guess + 10):
                    print('Very close')
                elif current_input in range(self.number_to_guess - 25, self.number_to_guess + 25)\
                        and current_input not in range(self.number_to_guess - 10, self.number_to_guess + 10):
                    print('Close')
                elif current_input in range(self.number_to_guess - 50, self.number_to_guess + 50)\
                        and current_input not in range(self.number_to_guess - 25, self.number_to_guess + 25):
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
        return current_input


test = guessing()
test.comparison()
