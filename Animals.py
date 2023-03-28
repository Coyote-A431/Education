import os
import re


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

current_path = get_path()

def get_file_list(current_path):
    animal_list = []
    with os.scandir(current_path) as files:
        for file in files:
            animal_list.append(file.name)
    print(animal_list)
    return animal_list

# get_file_list(current_path)

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

p = get_parsed_data(current_path)

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

    def __init__(self, name, genus, species, avg_lifetime, avg_height, avg_weight, place, country, file_name):
        self.name = name
        self.genus = genus
        self.species = species
        self.avg_lifetime = avg_lifetime
        self.avg_height = avg_height
        self.avg_weight = avg_weight
        self.place = place
        self.country = country
        self.file_name = file_name

    def __repr__(self):
        return self.name

    def info(self):
        attributes_dict = self.__dict__
        attributes_dict.pop('file_name')
        for attribute_name, attribute_value in attributes_dict.items():
            print(self.full_attribute_names_map[attribute_name] + ': ' + attribute_value)

def create_class_objects():
    parsed_animal_dict = get_parsed_data(current_path)
    animal_dict = {}
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
                        file_name=file_name,
                        )
        # TODO добавить обработку исключения, если в файле будут не все атрибуты
        animal_dict[index] = animal
        index += 1
    return animal_dict

animal_dict = create_class_objects()

def print_animal_dict(animal_dict):
    for animal_name in animal_dict.values():
        print(f'{animal_name}')

# print_animal_dict(animal_dict)

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
    animal_dict[user_input_int].info()

# show_animal_data(animal_dict)

def change_animal_data(animal_dict):
    is_correct_input_animal_num = False
    changed_animal_file_names_list = []
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
        index_for_inner_attributes = 1
        inner_attributes_dict = {}
        for attribute_name in Animal.full_attribute_names_map.keys():
            inner_attributes_dict[index_for_inner_attributes] = attribute_name
            index_for_inner_attributes += 1
        user_input_attribute = input()
        try:
            user_input_attribute_int = int(user_input_attribute)
            if user_input_attribute_int in range(1, index_for_outer_attributes + 1):
                is_correct_symbols = False
                while not is_correct_symbols:
                    new_animal_value = input('Введите новое значение: ')
                    if user_input_attribute_int in (1, 2, 3, 7):
                        is_rus_symbols = re.fullmatch('[а-яА-ЯёЁ\s]+', new_animal_value)
                        if is_rus_symbols:
                            is_correct_symbols = True
                        else:
                            print('Для данного пункта можно вводить только русские буквы')
                    elif user_input_attribute_int in (4, 5, 6):
                        if new_animal_value.isdigit():
                            is_correct_symbols = True
                        else:
                            print('Для данного пункта можно вводить только целые числа')
                    elif user_input_attribute_int == 8:
                        is_rus_symbols = re.fullmatch('[а-яА-ЯёЁ\s,]+', new_animal_value)
                        if is_rus_symbols:
                            is_correct_symbols = True
                        else:
                            print('Для данного пункта можно вводить только русские буквы и запятые')
                print('Применить корректировки (y/n)?')
                print('Значение до изменения: ',
                      getattr(animal_dict[user_animal_input_int], inner_attributes_dict[user_input_attribute_int]))
                print('Значение после изменения: ', new_animal_value)
                is_correct_yes_or_no = False
                while not is_correct_yes_or_no:
                    yes_or_no = input()
                    if yes_or_no == 'y':
                        setattr(animal_dict[user_animal_input_int], inner_attributes_dict[user_input_attribute_int],
                                new_animal_value)
                        if animal_dict[user_animal_input_int].file_name not in changed_animal_file_names_list:
                            changed_animal_file_names_list.append(animal_dict[user_animal_input_int].file_name)
                        is_correct_yes_or_no = True
                        is_correct_input_attribute_num = True
                    elif yes_or_no == 'n':
                        is_correct_yes_or_no = True
                    else:
                        print(f'Введите "Да" (y) или "Нет" (n) согласно регистру')
            else:
                raise ValueError
        except ValueError:
            print('Введён некорректный номер')
    return animal_dict[user_animal_input_int].file_name

# b = change_animal_data(animal_dict)

def save_and_exit(current_path, changed_animal_file_names_list):
    for index in animal_dict:
        if animal_dict[index].file_name in changed_animal_file_names_list:
            open(current_path + '\\' + animal_dict[index].file_name, 'w').close()
            for attribute_prog_name, attribute_name in Animal.full_attribute_names_map.items():
                with open(current_path + '\\' + animal_dict[index].file_name, 'a+', encoding='utf-8') as writer:
                    writer.write(f'{attribute_name}: {animal_dict[index].__dict__[attribute_prog_name]}\n')

# save_and_exit(current_path, changed_animal_file_names_list)

def main_menu():
    is_correct_point = False
    changed_animal_file_names_list = []
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
            if changed_animal not in changed_animal_file_names_list:
                changed_animal_file_names_list.append(changed_animal)
        elif user_main_menu_choice == '3':
            save_and_exit(current_path, changed_animal_file_names_list)
            is_correct_point = True
        elif user_main_menu_choice == '4':
            is_correct_point = True
        else:
            print('Введено некорректное значение')

main_menu()


# TODO setattr

# print(animal_dict.__dict__)

# q = int(input())
# dict = {}
# index = 1
# for attribute_name_rus in Animal.full_attribute_names_map.keys():
#     print(f'{index}: {attribute_name_rus}')
#     dict[index] = attribute_name_rus
#     index += 1
# print(dict)


