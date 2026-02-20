from .find_by_name import find_by_name
from .find_by_id import find_by_id

def change_contact_number(list_contacts):
     
     inp_name_contact_to_change_number = input('Введите имя контакта, номер которого хотите изменить: ').strip()
     found_contact_list = find_by_name(list_contacts, inp_name_contact_to_change_number)

     if not found_contact_list:
        print(f'Контакт {inp_name_contact_to_change_number} не найден!')
        return
     
     target_id = None
     if len(found_contact_list) == 1:
        target_id = found_contact_list[0]['id']
     else:
        print(f'Вот список контактов с именем {inp_name_contact_to_change_number}. Выберете ID контакта для изменения номера.')
        
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
        
     while True:
            inp_contact_number = input(f'Введите новый номер для контакта "{contact_to_change['name']}": ').strip()
            if inp_contact_number.isdigit():
                contact_to_change['number'] = int(inp_contact_number)
                print(f'Номер для контакта "{contact_to_change['name']}" успешно измнен!')
                break
            else:
                print('Номер должен состоять из чисел. Попробуйте снова.')