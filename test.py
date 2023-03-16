import random

class tst:

    def __init__(self):
        self.num_to_guess = self.rn()

    def rn(self):
        random_number = random.randint(1, 100)
        print(random_number)
        return random_number

    def valid(self):
        try:
            is_valid_input = False
            while not is_valid_input:
                try:
                    user_num = input('Guess the number: ')
                    current_input = int(user_num)
                    is_valid_input = True
                except ValueError:
                    print('You entered not number or left empty field')
        except KeyboardInterrupt:
            print('asdf')
        return current_input

    def comp(self, random_number, current_input):
        is_right_input = False
        is_first_iteration = True
        previous_input = -1
        while not is_right_input:
            current_input = self.valid()
            try:
                if current_input == self.num_to_guess:
                    print('You are great!')
                    is_right_input = True
                elif current_input in range(self.num_to_guess - 10, self.num_to_guess + 11):
                    print('Very close')
                elif current_input in range(self.num_to_guess - 25, self.num_to_guess + 26) \
                        and current_input not in range(self.num_to_guess - 10, self.num_to_guess + 11):
                    print('Close')
                elif current_input in range(self.num_to_guess - 50, self.num_to_guess + 51) \
                        and current_input not in range(self.num_to_guess - 25, self.num_to_guess + 26):
                    print('Far')
                else:
                    print('Very far')
                if not is_first_iteration:
                    if previous_input != current_input:
                        if previous_input < self.num_to_guess and not is_right_input:
                            if current_input > previous_input:
                                print('Closer')
                            else:
                                print('Further')
                        elif previous_input > self.num_to_guess and not is_right_input:
                            if current_input > previous_input:
                                print('Further')
                            else:
                                print('Closer')
                is_first_iteration = False
                previous_input = current_input
            except KeyboardInterrupt:
                print('smth')
        return current_input

    def func(self):
        try:
            self.comp(self.num_to_guess, self.valid())
        except KeyboardInterrupt:
            print('Fock')


# tst = tst()
# tst.func()
# tst.valid()
# tst.comp()

def test(a = False):
    if not a:
        print(1)
    else:
        print(2)

test(1)

