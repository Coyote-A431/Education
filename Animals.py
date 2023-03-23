import os


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


def get_parsed_data():
    user_path = r'C:\Users\Unknown\Desktop\Education\Animal'
    file_list = []
    with os.scandir(user_path) as files:
        for file in files:
            file_list.append(file.name)
    # files_locations = [f'{user_path}\\{animal}' for animal in animal_list]
    files_locations = {animal: f'{user_path}\\{animal}' for animal in file_list}
    # f = []
    # for animal in animal_list:
    #     f.append(f'{user_path}\\{animal}')
    animal_data_dict = {}  # Словарь {имя файла: значения файла в виде словаря}
    for file_name, path in files_locations.items():
        with open(path, 'r', encoding='utf-8') as reader:
            file_content = reader.read()
        animal_attributes_dict = {}  # Словарь с атрибутами животных {название атрибута: название значения}
        attribute_row = file_content.split('\n')
        for i in attribute_row:
            # attribute_value_list = i.split(':')
            attribute_name, attribute_value = i.split(':')
            attribute_name, attribute_value = attribute_name.strip(), attribute_value.strip()
            # attribute_name = i.split(':')[0]
            # attribute_value = i.split(':')[1]
            animal_attributes_dict[attribute_name] = attribute_value
        animal_data_dict[file_name] = animal_attributes_dict
    return animal_data_dict


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

    # def choose_option(self):
    #     current_path = self.get_path()
    #     current_file_list = self.get_file_list(current_path)
    #     is_corr = False
    #     while not is_corr:
    #         print('1) Вывести более подробную информацию о животном',
    #               '2) Скорректировать информацию',
    #               '3) Сохранить и выйти',
    #               '4) Выйти без сохранения', sep='\n')
    #         user_choice = int(input('Введите интересующий Вас пункт: '))
    #         if user_choice == 1 or user_choice == 2:
    #             user_animal = input('Выберите животное из списка: ')
    #             corr_anim = user_animal + '.txt'
    #             correct_path = current_path + '\\' + user_animal + '.txt'
    #             if corr_anim in current_file_list:
    #                 with open(correct_path, 'r', encoding='utf-8') as file:
    #                     a = file.read().splitlines()
    #                     print('\n'.join(a))
    #                     file.close()
    #         if user_choice == 4:
    #             is_corr = True

def create_class_objects():
    parsed_animal_dict = get_parsed_data()
    animal_dict = {}
    index = 1
    for file_name, animal_attributes in parsed_animal_dict.items():
        # print(animal_attributes)
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
    # print(animal_dict)
    return animal_dict

animal_dict = create_class_objects()

def print_animal_dict(animal_dict):
    for animal_number, animal_name in animal_dict.items():
        print(f'{animal_number}: {animal_name}')

def show_animal_data(animal_dict):
    is_correct_input = False
    user_input = ''
    print('Выберите животное из списка: ')
    for animal_number, animal_name in animal_dict.items():
        print(f'{animal_number}: {animal_name}')
    while not is_correct_input:
        user_input = input()
        try:
            user_input_int = int(user_input)
            if user_input_int in range(len(animal_dict)):
                is_correct_input = True
            else:
                raise ValueError
        except ValueError:
            print('Введён некорректный номер')
    animal_dict[user_input_int].info()

show_animal_data(animal_dict)







