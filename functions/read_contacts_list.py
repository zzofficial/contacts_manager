def read_contacts_list(list_contacts):
    for contact in list_contacts:
        print(f'Имя: {contact['name']} | Номер телефона: {contact['number']} | Заметка: {contact['keep']}')