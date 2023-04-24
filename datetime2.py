class datetime2:

    MONTHS_WITH_MAX_DAYS_SET = {1, 3, 5, 7, 8, 10, 12}

    CHINESE_CALENDAR = {0: 'monkey', 1: 'rooster', 2: 'dog', 3: 'pig', 4: 'rat', 5: 'bull', 6: 'tiger', 7: 'rabbit',
                        8: 'dragon', 9: 'snake', 10: 'horse', 11: 'sheep'}

    MONTHS = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    WEEK_DAYS = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

    DAYS_IN_MONTHS = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, random_date = False):
        self.random_date = random_date
        data_list = self.validation(random_date)
        self.day = data_list[0]
        self.month = data_list[1]
        self.year = data_list[2]
        self.date = data_list[3]

    def validation(self, random_date):
        if random_date:
            result = []
            random_year = random.randint(1970, 9999)
            random_month = random.randint(1, 12)
            if random_month in datetime2.MONTHS_WITH_MAX_DAYS_SET:
                random_day = random.randint(1, 31)
            elif random_month not in datetime2.MONTHS_WITH_MAX_DAYS_SET and random_month != 2:
                random_day = random.randint(1, 30)
            elif random_month == 2 and random_year % 100 % 4 == 0:
                random_day = random.randint(1, 29)
            else:
                random_day = random.randint(1, 28)
            random_date = str(random_day) + '.' + str(random_month) + '.' + str(random_year)
            result.append(random_day)
            result.append(random_month)
            result.append(random_year)
            result.append(random_date)
            return result
        else:
            is_valid_input = False
            while not is_valid_input:
                try:
                    user_date = input('Enter date in format dd.mm.yyyy: ')
                    string_list = user_date.split('.')
                    result = list(map(int, string_list))
                    if len(result) == 3:
                        local_day = result[0]
                        local_month = result[1]
                        local_year = result[2]
                        if len(result) == 3 and local_month > 0 and local_month < 13 and local_year >= 1970:
                           is_month_with_max_days = local_day in range(1, 32) \
                                                    and local_month in datetime2.MONTHS_WITH_MAX_DAYS_SET
                           is_month_with_min_days = local_day in range(1, 31) and local_month != 2 \
                                                    and local_month not in datetime2.MONTHS_WITH_MAX_DAYS_SET
                           is_feb_in_leap_year = local_day in range(1, 30) \
                                                 and (local_year % 100 != 0 and local_year % 4 == 0 or local_year % 400 == 0)
                           is_feb_in_not_leap_year = (local_year % 100 == 0 and local_year % 4 != 0 or local_year % 400 != 0) \
                                                     and local_day in range(1, 29)
                           if is_month_with_max_days or is_month_with_min_days or is_feb_in_leap_year \
                              or is_feb_in_not_leap_year:
                               result.append(user_date)
                               is_valid_input = True
                           else:
                               raise ValueError
                        else:
                            raise ValueError
                    else:
                        raise ValueError
                except ValueError:
                    print('You entered wrong date')
            return result

    def print_leap_year(self):
        if self.year % 100 % 4 == 0:
            leap_status = self.date + ' is leap year'
        else:
            leap_status = self.date + ' is not leap year'
        print(leap_status)

    def print_chinese_year(self):
        result_chinese_year = f'{self.year} is year of the {datetime2.CHINESE_CALENDAR[self.year % 12]}'
        print(result_chinese_year)

    def print_month(self):
        string_month = datetime2.MONTHS[self.month]
        print(string_month)

    def print_quarter(self):
        if self.month >= 1 and self.month <= 3:
            quarter = '1st quarter'
        elif self.month > 3 and self.month <= 6:
            quarter = '2nd quarter'
        elif self.month > 6 and self.month <= 9:
            quarter = '3rd quarter'
        else:
            quarter = '4th quarter'
        print(quarter)

    def print_day(self):
        print(self.day)

    def print_week_day(self):
        if self.month > 2:
            local_year = self.year
            local_month = self.month - 2
        else:
            local_year = self.year - 1
            local_month = 12 - abs(self.month - 2)
        first_year_nums = local_year // 100
        last_year_nums = local_year % 100
        week_day = (self.day + ((13 * local_month - 1) // 5) + last_year_nums + (last_year_nums // 4 + first_year_nums // 4 - 2 * first_year_nums + 777)) % 7
        print(datetime2.WEEK_DAYS[week_day])

    def print_number_day(self):
        number_day = 0
        iterator = 1
        while iterator < self.month:
            number_day += datetime2.DAYS_IN_MONTHS[iterator]
            iterator += 1
        if self.year % 100 % 4 != 0 and self.month > 2:
            number_day = number_day + self.day - 1
        else:
            number_day = number_day + self.day
        print(number_day)

    def all_func(self):
        self.print_leap_year()
        self.print_chinese_year()
        self.print_month()
        self.print_quarter()
        self.print_day()
        self.print_week_day()
        self.print_number_day()




test = datetime2()
test.all_func()


