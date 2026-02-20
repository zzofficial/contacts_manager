import json

def save_contacts_list(list_contacts):
    """
    Модуль, реализующий пользовательское сохранение
    
    """
    inp_file_name = input('Введите название файла: ')
    file_name = f'{inp_file_name}.json'
    with open(file_name, 'w', encoding='utf-8', ) as file:
        json.dump(list_contacts, file, indent=4, ensure_ascii=False)
        print(f'Файл контактов "{inp_file_name}" - успешно сохранен.')