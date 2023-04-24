class Factorial_Fibonacci:

    def __init__(self):
        self.num_for_fact, self.num_for_fib = self.validation()

    def validation(self):
        is_valid_input = False
        while not is_valid_input:
            try:
                user_num = input('Enter Fibonacci number/factorial number: ')
                user_num = int(user_num)
                if user_num > 0:
                    is_valid_input = True
                else:
                    print('Your number must be greater 0')
            except ValueError:
                print('You entered not number or left empty field')
        result = [user_num, user_num + 2]
        return result

    def get_fact_num(self):
        factorial = 1
        i = self.num_for_fact
        while i > 1:
            factorial *= i
            i -= 1
        print(f'{self.num_for_fact} iterations completed. Factorial {self.num_for_fact}! = ', factorial)
        return factorial

    def get_fib_num(self):
        fib1 = fib2 = 1
        i = 0
        while i < self.num_for_fib - 2:
            fib1, fib2 = fib2, fib1 + fib2
            i += 1
            print(f'{i} iteration: ', fib2)
        return fib2


if __name__ == '__main__':
    test = Factorial_Fibonacci()
    test.get_fib_num()
    test.get_fact_num()

