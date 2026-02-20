from .find_by_name import find_by_name
from .find_by_id import find_by_id

def del_contact(list_contacts):
    """
    Модуль, реализующий удаление контакта.
    Предусмотрена проверка на наличие контакта с введенным пользователем именем в БД.

    Поиск по БД реализован комбинированно: через имя,
    которое пользователю предлагается ввести самому, а после, при
    наличии нескольких пользователей с таким имеем, реализуется поиск
    по ID. Пользователю предлагается ввести необходимый из выпадающего списка.
    Предусмотрена проверка на валидность введенного ID.
    
    """
    inp_name_contact_to_delite = input('Введите имя контакта, которого хотите удалить: ').strip()
    found_contact_list = find_by_name(list_contacts, inp_name_contact_to_delite)

    target_id = None
    if not found_contact_list:
        print(f'Контакт {inp_name_contact_to_delite} не найден!')
        return
    
    if len(found_contact_list) == 1:
        target_id = found_contact_list[0]['id']
    else:
        print(f'Вот список контактов с имененм {inp_name_contact_to_delite}. Выберете ID контакта для удаления.')
        for contact in found_contact_list:
            print(f'Имя: {contact['name']} | Номер телефона: {contact['number']} | ID: {contact['id']}')

        while True:
            target_id = input('Введите ID контакта для удаления: ').strip()
            if not any(c['id'] == target_id for c in list_contacts):
                print('Неверный ID. Попробуйте еще раз.')
                continue
            break
    
    found_contact = find_by_id(list_contacts, target_id)

    if not found_contact:
        print(f'Критическая ошибка: контакт с ID "{target_id}" не найден.')
        return
    list_contacts.remove(found_contact)
    print(f'Контакт "{inp_name_contact_to_delite}" успешно удален.')