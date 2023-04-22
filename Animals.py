import os
import re


class Animal:
    full_attribute_names_map = {'name': 'Наименование',
                                'genus': 'Род',
                                'species': 'Вид',
                                'avg_lifetime': 'Средняя продолжительность жизни',
                                'avg_height': 'Средний рост',
                                'avg_weight': 'Средняя масса тела',
                                'place': 'Место обитания',
                                'country': 'Страна обитания',
                                }

    index_for_inner_attributes = 1
    inner_attributes_dict = {}
    for attribute_name in full_attribute_names_map.keys():
        inner_attributes_dict[index_for_inner_attributes] = attribute_name
        index_for_inner_attributes += 1

    def __init__(self,
                 name,
                 genus,
                 species,
                 avg_lifetime,
                 avg_height,
                 avg_weight,
                 place,
                 country,
                 ):
        self.__name = name
        self.__genus = genus
        self.__species = species
        self.__avg_lifetime = avg_lifetime
        self.__avg_height = avg_height
        self.__avg_weight = avg_weight
        self.__place = place
        self.__country = country

    def __repr__(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_animal_value):
        if re.fullmatch('[а-яА-ЯёЁ\s]+', new_animal_value):
            self.__name = new_animal_value
        else:
            print('Для данного пункта можно вводить только русские буквы')

    @property
    def genus(self):
        return self.__genus

    @genus.setter
    def genus(self, new_animal_value):
        if re.fullmatch('[а-яА-ЯёЁ\s]+', new_animal_value):
            self.__genus = new_animal_value
        else:
            print('Для данного пункта можно вводить только русские буквы')

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, new_animal_value):
        if re.fullmatch('[а-яА-ЯёЁ\s]+', new_animal_value):
            self.__species = new_animal_value
        else:
            print('Для данного пункта можно вводить только русские буквы')

    @property
    def avg_lifetime(self):
        return self.__avg_lifetime

    @avg_lifetime.setter
    def avg_lifetime(self, new_animal_value):
        if new_animal_value.isdigit():
            self.__avg_lifetime = new_animal_value
        else:
            print('Для данного пункта можно вводить только целые числа')

    @property
    def avg_height(self):
        return self.__avg_height

    @avg_height.setter
    def avg_height(self, new_animal_value):
        if new_animal_value.isdigit():
            self.__avg_height = new_animal_value
        else:
            print('Для данного пункта можно вводить только целые числа')

    @property
    def avg_weight(self):
        return self.__avg_weight

    @avg_weight.setter
    def avg_weight(self, new_animal_value):
        if new_animal_value.isdigit():
            self.__avg_weight = new_animal_value
        else:
            print('Для данного пункта можно вводить только целые числа')

    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, new_animal_value):
        if re.fullmatch('[а-яА-ЯёЁ\s]+', new_animal_value):
            self.__place = new_animal_value
        else:
            print('Для данного пункта можно вводить только русские буквы')

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_animal_value):
        if re.fullmatch('[а-яА-ЯёЁ\s,]+', new_animal_value):
            self.__country = new_animal_value
        else:
            print('Для данного пункта можно вводить только русские буквы и запятые')

    def info(self, user_input_int):
        for attribute_name, attribute_value in self.full_attribute_names_map.items():
            a = getattr(animal_dict[user_input_int], attribute_name)
            print(f'{attribute_value}: {a}')


def get_path():
    is_path_correct = False
    while not is_path_correct:
        try:
            user_path = input('Введите путь до нужного файла: ')
            num_files = len([f for f in os.listdir(user_path)
                             if os.path.isfile(os.path.join(user_path, f))])
            if num_files > 0:
                is_path_correct = True
            else:
                print('В введённом Вами пути не существует файлов')
        except FileNotFoundError:
            print('Вы ввели несуществующий путь до файла')
        except OSError:
            print('Вы ввели несуществующий путь до файла')
    return user_path


def get_file_list(current_path):
    animal_list = []
    with os.scandir(current_path) as files:
        for file in files:
            animal_list.append(file.name)
    # print(animal_list)
    return animal_list


def get_parsed_data(current_path):
    # current_path = r'C:\Users\Unknown\Desktop\Education\Animal'
    file_list = []
    with os.scandir(current_path) as files:
        for file in files:
            file_list.append(file.name)
    # files_locations = [f'{user_path}\\{animal}' for animal in animal_list]
    files_locations = {animal: f'{current_path}\\{animal}' for animal in file_list}
    # f = []
    # for animal in animal_list:
    #     f.append(f'{user_path}\\{animal}')
    animal_data_dict = {}  # Словарь {имя файла: значения файла в виде словаря}
    # file_content = ''
    for file_name, path in files_locations.items():
        with open(path, 'r', encoding='utf-8') as reader:
            file_content = reader.read()
            # for all_lines in reader:
            #     if all_lines != '':
            #         file_content += all_lines
        animal_attributes_dict = {}  # Словарь с атрибутами животных {название атрибута: название значения}
        attribute_row = file_content.split('\n')
        if attribute_row[-1] == '':
            attribute_row.pop(-1)
        # attribute_row.remove('')
        for i in attribute_row:
            # attribute_value_list = i.split(':')
            attribute_name, attribute_value = i.split(':')
            attribute_name, attribute_value = attribute_name.strip(), attribute_value.strip()
            # attribute_name = i.split(':')[0]
            # attribute_value = i.split(':')[1]
            animal_attributes_dict[attribute_name] = attribute_value
        animal_data_dict[file_name] = animal_attributes_dict
    return animal_data_dict


def create_class_objects():
    parsed_animal_dict = get_parsed_data(current_path)
    animal_dict = {}
    animal_file_name_dict = {}
    result = []
    index = 1
    for file_name, animal_attributes in parsed_animal_dict.items():
        animal = Animal(name=animal_attributes['Наименование'],
                        genus=animal_attributes['Род'],
                        species=animal_attributes['Вид'],
                        avg_lifetime=animal_attributes['Средняя продолжительность жизни'],
                        avg_height=animal_attributes['Средний рост'],
                        avg_weight=animal_attributes['Средняя масса тела'],
                        place=animal_attributes['Место обитания'],
                        country=animal_attributes['Страна обитания'],
                        )
        # TODO добавить обработку исключения, если в файле будут не все атрибуты
        animal_file_name_dict[index] = file_name
        animal_dict[index] = animal
        index += 1
    result.append(animal_dict)
    result.append(animal_file_name_dict)
    return result


def print_animal_dict(animal_dict):
    for animal_name in animal_dict.values():
        print(f'{animal_name}')


def show_animal_data(animal_dict):
    is_correct_input = False
    print('Выберите животное из списка: ')
    for animal_number, animal_name in animal_dict.items():
        print(f'{animal_number}: {animal_name}')
    while not is_correct_input:
        user_input = input()
        try:
            user_input_int = int(user_input)
            if user_input_int in range(1, len(animal_dict) + 1):
                is_correct_input = True
            else:
                raise ValueError
        except ValueError:
            print('Введён некорректный номер')
    animal_dict[user_input_int].info(user_input_int)


def change_animal_data(animal_dict):
    is_correct_input_animal_num = False
    print('Выберите животное из списка: ')
    for animal_number, animal_name in animal_dict.items():
        print(f'{animal_number}: {animal_name}')
    while not is_correct_input_animal_num:
        user_animal_input = input()
        try:
            user_animal_input_int = int(user_animal_input)
            if user_animal_input_int in range(1, len(animal_dict) + 1):
                is_correct_input_animal_num = True
            else:
                raise ValueError
        except ValueError:
            print('Введён некорректный номер')
    is_correct_input_attribute_num = False
    while not is_correct_input_attribute_num:
        print('Выберите пункт, который хотите изменить: ')
        index_for_outer_attributes = 1
        for attribute_name_rus in Animal.full_attribute_names_map.values():
            print(f'{index_for_outer_attributes}: {attribute_name_rus}')
            index_for_outer_attributes += 1
        user_input_attribute = input()
        try:
            user_input_attribute_int = int(user_input_attribute)
            if user_input_attribute_int in range(1, index_for_outer_attributes):
                is_corr_symb = False
                while not is_corr_symb:
                    new_animal_value = input('Введите новое значение: ')
                    print('Применить корректировки (y/n)?')
                    print('Значение до изменения: ',
                          getattr(animal_dict[user_animal_input_int],
                                  Animal.inner_attributes_dict[user_input_attribute_int]))
                    print('Значение после изменения: ', new_animal_value)
                    is_correct_yes_or_no = False
                    while not is_correct_yes_or_no:
                        yes_or_no = input()
                        if yes_or_no == 'y':
                            setattr(animal_dict[user_animal_input_int],
                                    Animal.inner_attributes_dict[user_input_attribute_int],
                                    new_animal_value)
                            if new_animal_value == getattr(animal_dict[user_animal_input_int],
                                                           Animal.inner_attributes_dict[user_input_attribute_int]):
                                is_corr_symb = True
                            is_correct_yes_or_no = True
                            is_correct_input_attribute_num = True
                        elif yes_or_no == 'n':
                            is_correct_yes_or_no = True
                            is_corr_symb = True
                        else:
                            print(f'Введите "Да" (y) или "Нет" (n) согласно регистру')
            else:
                raise ValueError
        except ValueError:
            print('Введён некорректный номер')
    return user_animal_input_int


def save_and_exit(current_path, changed_animal_file_names_set, animal_file_name_dict):
    for index in animal_dict.keys():
        if index in changed_animal_file_names_set:
            attribute_prog_name_index = 1
            new_full_string_info = ''
            for attribute_name in Animal.full_attribute_names_map.values():
                new_attribute_value = getattr(animal_dict[index],
                                              Animal.inner_attributes_dict[attribute_prog_name_index])
                new_single_string_info = attribute_name + ': ' + new_attribute_value + '\n'
                new_full_string_info += new_single_string_info
                attribute_prog_name_index += 1
            with open(current_path + '\\' + animal_file_name_dict[index], 'w', encoding='utf-8') as writer:
                writer.write(f'{new_full_string_info}')


def main_menu():
    is_correct_point = False
    changed_animal_file_names_set = set()
    while not is_correct_point:
        print('1: Вывести более подробную информацию о животном',
              '2: Скорректировать информацию',
              '3: Сохранить и выйти',
              '4: Выйти без сохранения',
              sep='\n')
        user_main_menu_choice = input()
        if user_main_menu_choice == '1':
            show_animal_data(animal_dict)
        elif user_main_menu_choice == '2':
            changed_animal = change_animal_data(animal_dict)
            changed_animal_file_names_set.add(changed_animal)
        elif user_main_menu_choice == '3':
            save_and_exit(current_path, changed_animal_file_names_set, animal_file_name_dict)
            is_correct_point = True
        elif user_main_menu_choice == '4':
            is_correct_point = True
        else:
            print('Введено некорректное значение')


current_path = get_path()

# get_file_list(current_path)

p = get_parsed_data(current_path)

animal_info_data_list = create_class_objects()
animal_dict = animal_info_data_list[0]
animal_file_name_dict = animal_info_data_list[1]

# print_animal_dict(animal_dict)

# show_animal_data(animal_dict)

# b = change_animal_data(animal_dict, animal_file_name_dict)

# save_and_exit(current_path, changed_animal_file_names_list)

main_menu()

