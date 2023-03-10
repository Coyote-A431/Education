CHINESE_CALENDAR = {0: 'monkey', 1: 'rooster', 2: 'dog', 3: 'pig', 4: 'rat', 5: 'bull', 6: 'tiger', 7: 'rabbit',
                    8: 'dragon', 9: 'snake', 10: 'horse', 11: 'sheep'}

MONTHS = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}

MONTHS_WITH_MAX_DAYS_SET = {1, 3, 5, 7, 8, 10, 12}

MONTH_INDEX_DICT = {1: 6, 2: 2, 3: 2, 4: 5, 5: 0, 6: 3, 7: 5, 8: 1, 9: 4, 10: 6, 11: 2, 12: 4}

WEEK_DAYS = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}

LEAP_YEAR_DAYS_IN_MONTH_DICT = {1: 31, 2: 60, 3: 91, 4: 121, 5: 152, 6: 182, 7: 213, 8: 244, 9: 274, 10: 305, 11: 335}

NO_LEAP_YEAR_DAYS_IN_MONTH_DICT = {1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304,
                                   11: 334}

def validation():
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
                if local_month > 0 and local_month < 13 and local_year >= 1970:
                    is_month_with_max_days = local_day in range(1, 32) and local_month in MONTHS_WITH_MAX_DAYS_SET
                    is_month_with_min_days = local_day in range(1, 31) and local_month != 2 \
                                             and local_month not in MONTHS_WITH_MAX_DAYS_SET
                    is_feb_in_leap_year = local_day in range(1, 30) \
                                          and (local_year % 100 != 0 and local_year % 4 == 0 or local_year % 400 == 0)
                    is_feb_in_not_leap_year = local_day in range(1, 29) \
                                              and (local_year % 100 == 0 and local_year % 4 != 0 or local_year % 400 != 0)
                    if is_month_with_max_days or is_month_with_min_days or is_feb_in_leap_year or is_feb_in_not_leap_year:
                        result.append(user_date)
                        is_valid_input = True
                    else:
                        print('You entered wrong date')
                else:
                    print('You entered wrong date')
            else:
                print('You entered wrong date')
        except ValueError:
            print('You entered wrong date')
    return result


def print_leap_year(year, date):
    if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        leap_status = date + ' is leap year'
    else:
        leap_status = date + ' is not leap year'
    print(leap_status)


def print_chinese_year(year):
    result_chinese_year = f'{year} is year of the {CHINESE_CALENDAR[year % 12]}'
    print(result_chinese_year)


def print_month(month):
    string_month = MONTHS[month]
    print(string_month)


def print_quarter(month):
    if month >= 1 and month <= 3:
        quarter = '1st'
    elif month > 3 and month <= 6:
        quarter = '2nd'
    elif month > 6 and month <= 9:
        quarter = '3rd'
    else:
        quarter = '4th'
    print(quarter + ' quarter')


def print_number_day(day, month, year):
    year_last_num = year % 100
    if month == 1:
        day_num = day
    else:
        if year_last_num % 4 == 0:
            day_num = LEAP_YEAR_DAYS_IN_MONTH_DICT[month - 1] + day
        else:
            day_num = NO_LEAP_YEAR_DAYS_IN_MONTH_DICT[month - 1] + day
    print(day_num)


def print_week_day(year, month, day):
    year_last_num = year % 100
    first_part_year_ind = year_last_num // 12
    second_part_year_ind = year_last_num % 12
    third_part_year_ind = second_part_year_ind // 4
    year_index = first_part_year_ind + second_part_year_ind + third_part_year_ind
    month_index = MONTH_INDEX_DICT[month]
    if year // 100 == 19:
        century_index = 1
    else:
        century_index = 0
    if year_last_num % 4 == 0 and (month == 1 or month == 2):
        leap_year_index = 1
    else:
        leap_year_index = 0
    week_num = (year_index + month_index + day + century_index - leap_year_index) % 7
    week_day = WEEK_DAYS[week_num]
    print(week_day)


###


date_list = validation()
day = date_list[0]
month = date_list[1]
year = date_list[2]
date = date_list[3]
print_leap_year(year, date)
print_chinese_year(year)
print_quarter(month)
print_month(month)
print(day)
print_number_day(day, month, year)
print_week_day(year, month, day)


###


class datetime2:

    MONTHS_WITH_MAX_DAYS_SET = {1, 3, 5, 7, 8, 10, 12}

    CHINESE_CALENDAR = {0: 'monkey', 1: 'rooster', 2: 'dog', 3: 'pig', 4: 'rat', 5: 'bull', 6: 'tiger', 7: 'rabbit',
                        8: 'dragon', 9: 'snake', 10: 'horse', 11: 'sheep'}

    MONTHS = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
              9: 'September', 10: 'October', 11: 'November', 12: 'December'}

    WEEK_DAYS = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}

    DAYS_IN_MONTHS = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self):
        data_list = self.validation()
        self.day = data_list[0]
        self.month = data_list[1]
        self.year = data_list[2]
        self.date = data_list[3]

    def validation(self):
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
                           print('You entered wrong date')
                    else:
                        print('You entered wrong date')
                else:
                    print('You entered wrong date')
            except ValueError:
                print('You entered wrong date')
        return result

    def print_leap_year(self):
        if self.year % 100 % 4 == 0:
            is_leap_year = True
            leap_status = self.date + ' is leap year'
        else:
            is_leap_year = False
            leap_status = self.date + ' is not leap year'
        print(is_leap_year)
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




test = datetime2()
test.print_leap_year()
test.print_chinese_year()
test.print_month()
test.print_quarter()
test.print_day()
test.print_week_day()
test.print_number_day()


