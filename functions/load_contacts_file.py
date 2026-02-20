import json

def load_contacts_file():
    """
    Модуль, реализующий загрузку списка контактов.

    Реализована обработка нескольких ошибок доступа к файлу.
    Передусмотрен возврат пустого списка, чтобы программа не завершалась
    
    """
    inp_file_name = input('Введите имя списка контактов: ')
    file_name = f'{inp_file_name}.json'
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            list_c = json.load(file)
            print(f'Файл {inp_file_name} - загружен!')
            return list_c
    except (FileNotFoundError, json.JSONDecodeError):
        print(f'Файл {inp_file_name} не найден или поврежден. Начинаем с пустого списка.')
        return []