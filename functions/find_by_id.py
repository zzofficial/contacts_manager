def find_by_id(list_contacts, contact_id):
    """
    Вспомогательный модуль с вынесенной логикой поиска по ID.

    Модуль используется только в рамках реализации логики других модулей, 
    без прямого доступа пользователя
    """
    for contact in list_contacts:
        if contact['id'] == contact_id:
            return contact
    return None
