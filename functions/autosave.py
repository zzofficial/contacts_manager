import json

def autosave(list_contacts, file_name):
    """
    Модуль, реализующий логику автосохранения
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(list_contacts, file, indent=4)