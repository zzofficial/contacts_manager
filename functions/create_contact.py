import uuid

def create_contact(list_contacts, keep=None):
    inp_contact_name = input('Введите имя контакта: ')
    new_contact = {}
    new_id = str(uuid.uuid4())
    new_contact['id'] = new_id
    new_contact['name'] = inp_contact_name
    while True:
        inp_contact_number = input('Введите номер контакта: ')
        if inp_contact_number.isdigit():
            number = int(inp_contact_number)
            new_contact['number'] = number
            break
        else:
            print('Некорректный номер!')
    while True:
        inp_contact_keep_question = input('Хотели бы добавить заметку (y/n): ')
        if inp_contact_keep_question == 'y':
            inp_contact_keep_text = input('Введите текст заметки: ')
            new_contact['keep'] = inp_contact_keep_text
            break
        elif inp_contact_keep_question == 'n':
            new_contact['keep'] = keep
            break
        else:
            print('Некорректный ответ!')
    list_contacts.append(new_contact)
    print(f'Контакт с именем "{new_contact["name"]}" - успешно создан!')