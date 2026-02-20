from .find_by_name import find_by_name
from .find_by_id import find_by_id

def change_contact_keep(list_contacts):

    """
    Модуль реализующий изменение заметки контакта из книги.
    Предусмотрена проверка на наличие контакта в БД.

    Поиск по БД реализован комбинированно: через имя,
    которое пользователю предлагается ввести самому, а после, при
    наличии нескольких пользователей с таким имеем, реализуется поиск
    по ID. Пользователю предлагается ввести необходимый из выпадающего списка.
    Предусмотрена проверка на валидность введенного номера.

    """

    inp_name_contact_to_change = input('Введите имя контакта, заметку о котором хотите изменить: ').strip()
    found_contact_list = find_by_name(list_contacts, inp_name_contact_to_change)
    target_id = None

    if not found_contact_list: # логика, если введенное имя контакта отсутствует в БД
        print(f'Контакт {inp_name_contact_to_change} не найден!')
        return

    if len(found_contact_list) == 1: # логика, если введенное имя уникально
        target_id = found_contact_list[0]['id']
    else: # логика, если введенное имя повторяется 2 и более раз
        print(f'Вот список контактов с именем {inp_name_contact_to_change}. Выберете ID контакта для изменения заметки.')


        for contact in found_contact_list:
            print(f'Имя: {contact['name']} | Номер телефона: {contact['number']} | ID: {contact['id']}')

        while True:
            target_id = input('Введите ID нужного контакта: ').strip()
            if not any(c['id'] == target_id for c in found_contact_list):
                print('Неверный ID. Попробуйте еще раз.')
                continue
            break

    contact_to_change = find_by_id(list_contacts, target_id)

    if not contact_to_change:
        print(f'Критическая ошибка: контакт с ID "{target_id}" не найден.')
        return
            
    inp_new_contact_keep = input(f'Введите новую заметку для контакта "{contact_to_change['name']}": ').strip()
    contact_to_change['keep'] = inp_new_contact_keep
    print('Заметка успешно изменена!')


