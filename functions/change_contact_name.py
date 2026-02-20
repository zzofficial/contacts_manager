from .find_by_name import find_by_name
from .find_by_id import find_by_id

def change_contact_name(list_contacts):
    """
    Модуль, реализующий изменение имени контакта.
    Предусмотрена проверка на наличие контакта с введенным пользователем именем в БД.

    Поиск по БД реализован комбинированно: через имя,
    которое пользователю предлагается ввести самому, а после, при
    наличии нескольких пользователей с таким имеем, реализуется поиск
    по ID. Пользователю предлагается ввести необходимый из выпадающего списка.
    Предусмотрена проверка на валидность введенного ID.
    
    """
    inp_name_contact_to_change = input('Введите имя контакта, которое хотите изменить: ').strip()
    found_contact_list = find_by_name(list_contacts, inp_name_contact_to_change)

    target_id = None

    if not found_contact_list:
        print(f'Контакт с именем "{inp_name_contact_to_change}" не найден!')
        return

    if len(found_contact_list) == 1:
        target_id = found_contact_list[0]['id']
    
    else:
        print(f'Вот список контактов с имененм {inp_name_contact_to_change}. Выберете ID контакта изменения имени.')
        for contact in found_contact_list:
            print(f'Имя: {contact['name']} | Номер телефона: {contact['number']} | ID: {contact['id']}')

        while True:
            targer_id = input('Введите ID контакта для удаления: ').strip()
            if not any(c['id'] == targer_id for c in found_contact_list):
                print('Неверный ID. Попробуйте еще раз.')
                continue
            break

    found_contact = find_by_id(list_contacts, targer_id)
    if not found_contact:
        print(f'Критическая ошибка: контакт с ID "{target_id}" не найден.')
        return

    inp_new_contact_name = input(f'Введите новое имя для контакта "{found_contact['name']}": ').strip()
    found_contact['name'] = inp_new_contact_name
    print(f'Имя контакта "{inp_name_contact_to_change}" успешно измененно на "{inp_new_contact_name}".')