from functions import *
def main():
    print('//////////////////////////////')
    print('//...Ваш список контактов...//')
    print('//////////////////////////////')
    run = True
    contacts = []
    autosave_name = 'autosave.json'
    while run:
        clear_screen()
        print('//////////////////////////////')
        print('//...Ваш список контактов...//')
        print('//////////////////////////////')
        print('\nНажмите "1", чтобы вывести список контактов')
        print('Нажмите "2", чтобы добавить новый контакт')
        print('Нажмите "3", чтобы удалить контакт')
        print('Нажмите "4", чтобы изменить имя контакта')
        print('Нажмите "5", чтобы изменить номер контакта')
        print('Нажмите "6", чтобы изменить заметку контакта')
        print('Нажмите "7", чтобы сохранить список контактов')
        print('Нажмите "8", чтобы загрузить список контактов')
        print('Нажмите "9", чтобы выйти из списка контактов\n')
        inp = input('===> ')
        
        if inp == '1':
            read_contacts_list(contacts)
            input('\n Нажмите Enter, чтобы вернуться в меню...')
            
        elif inp == '2':
            create_contact(contacts)
            autosave(contacts, autosave_name)
            input('\n Нажмите Enter, чтобы вернуться в меню...')
        
        elif inp == '3':
            del_contact(contacts)
            autosave(contacts, autosave_name)
            input('\n Нажмите Enter, чтобы вернуться в меню...')
        
        elif inp == '4':
            change_contact_name(contacts)
            autosave(contacts, autosave_name)
            input('\n Нажмите Enter, чтобы вернуться в меню...')
        
        elif inp == '5':
            change_contact_number(contacts)
            autosave(contacts, autosave_name)
            input('\n Нажмите Enter, чтобы вернуться в меню...')

        elif inp == '6':
            change_contact_keep(contacts)
            autosave(contacts, autosave_name)
            input('\n Нажмите Enter, чтобы вернуться в меню...')

        elif inp == '7':
            save_contacts_list(contacts)
            input('\n Нажмите Enter, чтобы вернуться в меню...')

        elif inp == '8':
            loaded_contacts = load_contacts_file()
            if loaded_contacts is not None:
                contacts = loaded_contacts
                print('\n Контакты успешно загружены!')
            else:
                print('\n Ошибка: файл контактов не найден или поврежден!')
            input('\n Нажмите Enter, чтобы вернуться в меню...')
        
        elif inp == '9':
            exit_question = input('Вы хотели бы воспользоваться автосохранением (y/n): ')
            if exit_question == 'y':
                autosave(contacts, autosave_name)
                print('Ваши контакты автоматически сохранены.')
            print('До встречи!')
            run = False
        
        else:
            print('Неверная команда!')
            input('\n Нажмите Enter, чтобы попробовать снова...')


if __name__ == '__main__':
    main()